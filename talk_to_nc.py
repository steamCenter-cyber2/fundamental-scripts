import socket


s = socket.socket()

s.connect(("127.0.0.1",9001))
s.send(b"hello from python")