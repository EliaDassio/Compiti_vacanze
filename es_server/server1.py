import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind(('0.0.0.0',5000))
s.listen()
conn, addr = s.accept()

while True:
    data = conn.recv(4096)
    print(data)
    s.sendall(data)

conn.close()