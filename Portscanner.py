import os
Import sys
import random
import socket
Port = []
def lists():
   global Port
   for I in range(1200):
          if l >= 1200:
                break
          else:
                  Port.append(l)
def scanner(host):
         sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         for p in Port:
                  s = p
                  try:
                         sock.connect((host,p))                        sock.connect((host,p))
                  except:
                     Port.remove(s)
         for w in Port:
               print(“%s port number :  %d is open”%(host,Port))
         print(“scan compiled “)
         return
def main():
           host = str(input(“Host: “))
           lists()
           scanner(host)
if  __name__ == “__main__”:
                main()
                sys.exit()
