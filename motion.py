#!/usr/bin/python
# _*_ coding: utf-8 -*-

import time
import RobotApi
import json
import robotname as rn

##########################################
# move: takes the primitive movement name
# movement: fl -- forward left 
#           fr -- forward right
#           sl -- sidestep left
#           sr -- sidestep right
##########################################
def move(movement):
    RobotApi.ubtRobotInitialize()

    gIPAddr = ""
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
    if (movement == "fl"):
        filename = "angle_f.txt"
        start_number = 0
        end_number = 10
    elif (movement == "fr"):
        filename = "angle_f.txt"
        start_number = 11
        end_number = 17
    elif (movement == "sl"):
        print("left")
        filename = "angle_lside.txt"
        start_number = 0
        end_number = 2
    elif (movement == "sr"):
        print("right")
        filename = "angle_rside.txt"
        start_number = 0
        end_number = 2
    elif (movement == "r"):
        print("reset")
        filename = "angle_reset.txt"
        start_number = 0
        end_number = 2
    elif (movement == "f"):
        print("forward")
        move("fr")
        move("fl")
        return
    else:
        print("Please use the correct primitive movement name! " + movement + " is invalid")
        RobotApi.ubtRobotDisconnect("SDK" ,"1", gIPAddr)
        RobotApi.ubtRobotDeinitialize()
        exit(1)

    with open(filename, 'r') as infile:
        data = json.load(infile)
        ii = start_number
        while True:
            try:
                angle = data[str(ii)]
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
                ii += 1
                print(ii)
                time.sleep(1)
                if(ii > end_number):
                   break 
            except KeyError:
                print("key error")
                break

    RobotApi.ubtRobotDisconnect("SDK" ,"1", gIPAddr)
    #RobotApi.ubtRobotDeinitialize()
