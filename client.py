import socket
import time

s = socket.socket()
host = '10.0.0.34'
port = 12345
s.connect((host, port))
print(s.recv(1024))
time.sleep(3)
s.close()
