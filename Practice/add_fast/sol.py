import socket

s = socket.socket()
s.connect(("127.0.0.1", 9004))

for i in range(100):
    eq = s.recv(1024)
    print(eq)
    eq = str(eq).split(" ")
    result = int(eq[2]) + int(eq[6])
    s.send(str(result).encode())

print(s.recv(1024))
