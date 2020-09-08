#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import String, Float64

class JointControllerSine:
    def __init__(self, jointValue):
        self.start = rospy.get_rostime()
        self.now = rospy.get_rostime()
        self.curPose = 0
        jointTopic = '/robot/joint' + str(jointValue) + '_position_controller/command'
        
        self.pub = rospy.Publisher(jointTopic, Float64, queue_size=10)

    def sineFunction(self):
        self.now = rospy.get_time()

        self.pub.publish(math.sin(self.now))


def main():
    jointValue = 1
    # Init ROS node
    rospy.init_node('jointControllerSine', anonymous=True,  disable_signals=True)
    jointControllerSine = JointControllerSine(jointValue)
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
