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

data = {}
ii = 0
while(ii < 100):
        ret = RobotApi.ubtGetRobotServo(servoinfo) 
	angle = [servoinfo.SERVO1_ANGLE, servoinfo.SERVO2_ANGLE, servoinfo.SERVO3_ANGLE, servoinfo.SERVO4_ANGLE, servoinfo.SERVO5_ANGLE, servoinfo.SERVO6_ANGLE, servoinfo.SERVO7_ANGLE, servoinfo.SERVO8_ANGLE, servoinfo.SERVO9_ANGLE, servoinfo.SERVO10_ANGLE, servoinfo.SERVO11_ANGLE, servoinfo.SERVO12_ANGLE, servoinfo.SERVO13_ANGLE, servoinfo.SERVO14_ANGLE, servoinfo.SERVO15_ANGLE, servoinfo.SERVO16_ANGLE, servoinfo.SERVO17_ANGLE]
	data[ii] = angle
        print(angle)
	ii += 1
        time.sleep(0.1)

with open('angle_init.txt', 'w') as outfile:
	json.dump(data, outfile)
