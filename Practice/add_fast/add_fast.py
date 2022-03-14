import socket
from _thread import *
from random import randint as rand
from math import gcd
import time


host = "0.0.0.0"
port = 9004
global s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))
    exit()

s.listen(5)


def threaded_client(conn):
    starttime = time.time()

    for i in range(100):
        a = rand(1000, 100000000000)
        b = rand(1000, 100000000000)
        sol = str(a + b)

        conn.send("a = {} , b = {} \n".format(str(a), str(b)).encode())
        # conn.send("Give my you answer: ".encode())

        ret = conn.recv(100).decode("utf-8").strip()

        if ret != sol:
            conn.send("Sorry but I think you are bad at math :(".encode())
            conn.close()
            return

    conn.send(
        "Good job man! \nHere is your flag: flag{socket_prgramming_is_cool}".encode()
    )
    conn.close()


if __name__ == "__main__":
    while True:
        conn, addr = s.accept()
        print("connected to {}: {}".format(addr[0], addr[1]))
        start_new_thread(threaded_client, (conn,))
