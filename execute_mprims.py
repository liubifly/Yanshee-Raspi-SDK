import rospy
import motion
from std_msgs.msg import String

def callback(data):
    motion.move(data.data)

def listener():
    rospy.init_node("listener")
    rospy.Subscriber("actions", String, callback)
    rospy.spin()

if __name__ == "__main__":
    listener()
