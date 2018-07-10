#!/usr/bin/python
# _*_ coding: utf-8 -*-

import time
import RobotApi
import json
import socket

PI = 3.1415926

RobotApi.ubtRobotInitialize()

gIPAddr = ""
HOST = '192.168.1.108'
PORT = 8090
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

robotinfo = RobotApi.UBTEDU_ROBOTINFO_T()
robotinfo.acName = "Yanshee_4495"
ret = RobotApi.ubtRobotDiscovery("SDK", 15, robotinfo)
if (0 != ret):
        print("Return value :%d" % ret)
        exit(1)

gIPAddr = robotinfo.acIPAddr
ret = RobotApi.ubtRobotConnect("SDK", "1", gIPAddr)
if (0 != ret):
        print("Cannot connect to robot %s" % robotinfo.acName)
        exit(1)

servoinfo = RobotApi.UBTEDU_ROBOTSERVO_T()

while True:
	data = conn.recv(512)
        if not data: break
        try:
            angle = json.loads(data)
            joint_angles = angle['position']
            print joint_angles
	    angle = [float(i)/PI*180.0 for i in joint_angles]
       
            servoinfo.SERVO17_ANGLE = int(-angle[0]+90.0)
            #servoinfo.SERVO4_ANGLE = angle[1]
            #servoinfo.SERVO5_ANGLE = angle[2]
            #servoinfo.SERVO6_ANGLE = angle[3]
            servoinfo.SERVO12_ANGLE = int(angle[4]+90.0)
            servoinfo.SERVO13_ANGLE = int(angle[5]+65.0)
            servoinfo.SERVO14_ANGLE = int(-angle[6]+25.0)
            servoinfo.SERVO15_ANGLE = int(-angle[7]+90.0)
            servoinfo.SERVO16_ANGLE = int(angle[8]+90.0)
            servoinfo.SERVO1_ANGLE = int(-angle[9]+90.0)
            servoinfo.SERVO2_ANGLE = int(angle[10]+180.0)
            servoinfo.SERVO3_ANGLE = int(angle[11]+90.0)
            servoinfo.SERVO7_ANGLE = int(angle[12]+90.0)
            servoinfo.SERVO8_ANGLE = int(-angle[13]+90.0)
            servoinfo.SERVO9_ANGLE = int(angle[14]+150.0)
            servoinfo.SERVO10_ANGLE = int(angle[15]+90.0)
            servoinfo.SERVO11_ANGLE = int(angle[16]+90.0)
            ret = RobotApi.ubtSetRobotServo(servoinfo, 40)
        except:
            print 'json error'
	
RobotApi.ubtRobotDisconnect("SDK" ,"1", gIPAddr)
RobotApi.ubtRobotDeinitialize()
conn.close()
