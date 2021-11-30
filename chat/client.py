import socket as sck
s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
print("connected")
nickname = input("chouse your nickname: ")
msg = f"nickname:{nickname}" 
s.sendto(msg.encode(),('localhost',5000))
data,addr = s.recvfrom(4096)
msg = data.decode().split(",")
if (msg[0] == "OK"):
    while(True):
        print(msg[0])
        nick_reciver = input("how do you want to write to: ")
        messsage     = input("what do you want to write? : ")
        msg = f"sender:{nickname},recever:{nick_reciver},{messsage}"
        msg = data.decode().split(",")
s.close()