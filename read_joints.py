#!/usr/bin/env python

import yaml
import sys
import socket
import json

HOST = '192.168.1.108'    # The remote host
PORT = 8090              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

for doc in yaml.safe_load_all(sys.stdin):
	msg = {}
	msg['position'] = doc['position']
	#msg = ','.join(str(x) for x in doc['position'])
	s.send(json.dumps(msg))
	print (json.dumps(msg))

#	data = s.recv(1024)
s.close()
#	print 'Received', repr(data)
