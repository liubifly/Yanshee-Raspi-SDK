import motion
import socket

CONNECTION_LIST = [] # list of socket clients
REVC_BUFFER = 4096
PORT = 8080
HOST = '192.168.1.108'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(HOST, PORT)
except socket.error as msg:
    print "Bind failed. Error code: " + str(msg[0] + "Message" + msg[1])
    exit(1)

s.listen(5)
print "socket binds successfully, and is listening now."

conn, addr = s.accept()
print "Connected with " + addr[0] + str(addr[1]) 

while True:
	

s.close()
motion.move("fr")
