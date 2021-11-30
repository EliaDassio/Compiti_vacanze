import socket as sck
import sqlite3
nicknamedictionary = {}
s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
s.bind(('localhost',3000))
while(True):
    data, addr = s.recvfrom(4096)
    msg = data.decode().split(":")
    connection = sqlite3.connect('datanick.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO stocks VALUES ('','','')")
    connection.commit() 
    connection.close()
    
    #if (msg[0] == "nickname"):
    #    nicknamedictionary[addr] = msg[1]
    #    s.sendto("OK", msg[addr])
    #else:
    #    tmp = data.decode().split(",")
    #    reciver = tmp[1].slpit(":")
    #    s.sendto(tmp[2].encode(),(nicknamedictionary[reciver[1]]))
    #    print(f"I send a message {tmp[2]} a {nicknamedictionary[reciver[1]]}")
s.close()