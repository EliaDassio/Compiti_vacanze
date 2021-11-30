import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
stringa = "- - - "
s.connect(('localhost', 80))

while True:
    s.sendto(stringa.encode(),('',5000))
    data,addr = s.recvfrom(4096)

s.close()