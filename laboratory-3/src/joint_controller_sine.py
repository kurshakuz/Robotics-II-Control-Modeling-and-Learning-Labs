#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import String, Float64

class JointControllerSine:
    def __init__(self):
        self.start = rospy.get_rostime()
        self.now = rospy.get_rostime()
        self.curPose = 0
        
        self.pub = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=10)

    def sineFunction(self):
        self.now = rospy.get_time()

        self.pub.publish(math.sin(self.now))



def main():
    # Init ROS node
    rospy.init_node('jointControllerSine', anonymous=True,  disable_signals=True)
    jointControllerSine = JointControllerSine()
    while True:
        jointControllerSine.sineFunction()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo('shutting down')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
