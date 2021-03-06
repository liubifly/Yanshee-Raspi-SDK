#!/usr/bin/python
# _*_ coding: utf-8 -*-

import time
import RobotApi
import json
import socket
import servo_conversions as sc
import robotname as rn

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
robotinfo.acName = rn.getname() 
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
            # angle = {'position': [0]*17}
            joint_angles = angle['position']
            # print joint_angles
            angle = sc.rviz_to_yanshee(joint_angles)
            servoinfo.SERVO1_ANGLE = angle[0]
            servoinfo.SERVO2_ANGLE = angle[1]
            servoinfo.SERVO3_ANGLE = angle[2]
            servoinfo.SERVO4_ANGLE = angle[3]
            servoinfo.SERVO5_ANGLE = angle[4]
            servoinfo.SERVO6_ANGLE = angle[5]
            servoinfo.SERVO7_ANGLE = angle[6]
            servoinfo.SERVO8_ANGLE = angle[7]
            servoinfo.SERVO9_ANGLE = angle[8]
            servoinfo.SERVO10_ANGLE = angle[9]
            servoinfo.SERVO11_ANGLE = angle[10]
            servoinfo.SERVO12_ANGLE = angle[11]
            servoinfo.SERVO13_ANGLE = angle[12]
            servoinfo.SERVO14_ANGLE = angle[13]
            servoinfo.SERVO15_ANGLE = angle[14]
            servoinfo.SERVO16_ANGLE = angle[15]
            servoinfo.SERVO17_ANGLE = angle[16]
            ret = RobotApi.ubtSetRobotServo(servoinfo, 20)
        except:
            print 'json error'
	
RobotApi.ubtRobotDisconnect("SDK" ,"1", gIPAddr)
RobotApi.ubtRobotDeinitialize()
conn.close()
