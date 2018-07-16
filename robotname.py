import socket

def getname():
    mac_addr = socket.gethostname()[-4:]
    return "Yanshee_" + mac_addr
