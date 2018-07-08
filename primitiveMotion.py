import motion
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(HOST, PORT)
except socket.error as msg:
    print "Bind failed. Error code: " + str(msg[0] + "Message" + msg[1])
    exit(1)

s.listen(5)
print "socket binds successfully, and is listening now."

while True:
    conn, addr = s.accept()
    print "Connected with " + addr[0] + str(addr[1]) 
    s.recv(     ) 
s.close()
motion.move("fr")
