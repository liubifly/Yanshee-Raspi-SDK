from math import pi

def rviz_to_yanshee(angles_in):
    angle = [float(i)/pi*180.0 for i in angles_in]
    newangles = [0] * 18
    newangles[0] = int(-angle[9] + 90)
    newangles[1] = int(angle[10] + 180)
    newangles[2] = int(angle[11] + 90)
    newangles[3] = int(angle[1] + 90)
    newangles[4] = int(angle[2] + 2)
    newangles[5] = int(angle[3] + 90)
    newangles[6] = int(angle[12] + 90)
    newangles[7] = int(-angle[13] + 90)
    newangles[8] = int(angle[14] + 150)
    newangles[9] = int(angle[15] + 90)
    newangles[10] = int(angle[16] + 90)
    newangles[11] = int(angle[4] + 90)
    newangles[12] = int(angle[5] + 65)
    newangles[13] = int(-angle[6] + 25)
    newangles[14] = int(-angle[7] + 90)
    newangles[15] = int(angle[8] + 90)
    newangles[16] = int(-angle[0] + 90)
    return newangles

def yanshee_to_rviz(angles):
    newangles = [0] * 18
    newangles[9] = 90 - angles[0]
    newangles[10] = angles[1] - 180
    newangles[11] = angles[2] - 90
    newangles[1] = angles[3] - 90
    newangles[2] = angles[4] - 2
    newangles[3] = angles[5] - 90
    newangles[12] = angles[6] - 90
    newangles[13] = 90 - angles[7]
    newangles[14] = angles[8] - 150
    newangles[15] = angles[9] - 90
    newangles[16] = angles[10] - 90
    newangles[4] = angles[11] - 90
    newangles[5] = angles[12] - 65
    newangles[6] = 25 - angles[13]
    newangles[7] = 90 - angles[14]
    newangles[8] = angles[15] - 90
    newangles[0] = 90 - angles[16]
    angles_out = [float(i)/180*pi for i in newangles]
    return angles_out

