#!/usr/bin/python
# _*_ coding: utf-8 -*-


import time
import RobotApi

    

#------------------------------Connect-------------------------------------
RobotApi.ubtRobotInitialize()

<<<<<<< HEAD

robotname = "Yanshee_8F83"
gIPAddr = ""
=======
#The robot name you want to connect
robotname="Yanshee_8F83"
gIPAddr = "127.0.0.1"
>>>>>>> a94ade32ce46fa78895bfaeb439f10a80af73c12

robotinfo = RobotApi.UBTEDU_ROBOTINFO_T()
ret = RobotApi.ubtRobotDiscovery(1, "sdk", robotinfo)
if (0 != ret):
	print ("Return value: %d" % ret)
	exit(1)
if (robotinfo.acName == robotname):
	timeout = 0
else:
<<<<<<< HEAD
    timeout = 20


#Repeat searching 20
    
while(timeout!=0):
    ret = RobotApi.ubtRobotDiscovery(0,"SDK", robotinfo)
    if ret != 0:
        print("Can not Discover Robot (timeout)! Error code: %d." % ret)
        exit(timeout)
    print("Robot Name: %s" % robotinfo.acName)
    print("Robot IP: %s" % robotinfo.acIPAddr)
    time.sleep(1)
    timeout = timeout - 1
    if robotinfo.acName == robotname:
        gIPAddr = robotinfo.acIPAddr
        break
#print("gIPAddr = %s." % gIPAddr)

ret = RobotApi.ubtRobotConnect("sdk", "1" , gIPAddr)
if ret != 0:
    print("Can not connect to robot %s" % robotname)
    exit(2)


=======
	timeout = 255
# Search the robot
while (0 != timeout):
	ret = RobotApi.ubtRobotDiscovery(0, "sdk", robotinfo)
	if (0 != ret):
		print ("Return value: %d" % ret)
		break

	print ("Name: %s" % (robotinfo.acName))
	print ("IP: %s" % (robotinfo.acIPAddr))
	if (robotinfo.acName == robotname):
		gIPAddr = robotinfo.acIPAddr
		break
	time.sleep(1)
        timeout -= 1

print "gIPAddr = %s" %(gIPAddr)
ret = RobotApi.ubtRobotConnect("sdk", "1", gIPAddr)
if (0 != ret):
	print ("Return value: %d" % ret)
	exit(1)
>>>>>>> a94ade32ce46fa78895bfaeb439f10a80af73c12


#-----------------------------Getrobotstatus---------------------------------
#-----------------------------Volumeinformation------------------------------
status_info = RobotApi.UBTEDU_ROBOTINFRARED_SENSOR_T()
#status_info = RobotApi.UBTEDU_ROBOT_Battery_T()
#StatusList=[1,2,3,4,5,6]
print("Initialization Value: %d" % status_info.iValue)
ret = RobotApi.ubtGetRobotStatus(2,status_info)
if ret != 0:
    print("Can not get volume information. Error code: %d" % ret)
    exit(4)
else:
    print("Value: %d" % status_info.iValue)
#battery_info = int()
#for status in StatusList:
 #   print("status:%d \t value(init): %d" % (status,status_info.iValue))
  #  ret = RobotApi.ubtGetRobotStatus(status,status_info)
   # if ret != 0:
    #    print("status:%d \t Can not get information. Error code: %d" % (status,ret))
        #exit(3)
     #   continue
    #for value in status_info.iValue:
     #   print("status:%d \t Value: %d" % (status,value))

#---------------------------Disconnect--------------------------------------
RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()
