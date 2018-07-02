#!/usr/bin/python
# _*_ coding: utf-8 -*-

import time
import RobotApi
import json

RobotApi.ubtRobotInitialize()

gIPAddr = ""

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

ret = RobotApi.ubtGetRobotServo(servoinfo)

data = {}
i = 0
while(i < 1000):
	angle = [servoinfo.SERVO1, servoinfo.SERVO2, servoinfo.SERVO3, servoinfo.SERVO4, servoinfo.SERVO5, servoinfo.SERVO6, servoinfo.SERVO7, servoinfo.SERVO8, servoinfo.SERVO9, servoinfo.SERVO10, servoinfo.SERVO11, servoinfo.SERVO12, servoinfo.SERVO13, servoinfo.SERVO14, servoinfo.SERVO15, servoinfo.SERVO16, servoinfo.SERVO17]
	data[i] = angle
	i += 1

with open('angle_test.txt', 'w') as outfile:
	json.dump(data, outfile)
