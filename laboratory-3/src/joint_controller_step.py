#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Float64

class JointControllerStep:
    def __init__(self):
        self.start = rospy.get_rostime()
        self.now = rospy.get_rostime()
        self.curPose = 0
        
        self.pub = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=10)

    def stepFunction(self):
        self.now = rospy.get_rostime()

        if (self.now.secs - self.start.secs) >= 10:
            rospy.loginfo('changing pose')
            self.start = rospy.get_rostime()
            if self.curPose == 0:
                self.pub.publish(1.0)
                self.curPose = 1
            else:
                self.pub.publish(-1.0)
                self.curPose = 0
        else:
            if self.curPose == 0:
                self.pub.publish(-1.0)
            else:
                self.pub.publish(1.0)


def main():
    # Init ROS node
    rospy.init_node('jointControllerStep', anonymous=True,  disable_signals=True)
    jointControllerStep = JointControllerStep()
    while True:
        jointControllerStep.stepFunction()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo('shutting down')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
