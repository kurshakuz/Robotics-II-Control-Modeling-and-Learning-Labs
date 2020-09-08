#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Float64

class JointControllerIncrementer:
    def __init__(self, jointValue):
        self.oldVals = None
        jointTopic = '/robot/joint' + str(jointValue) + '_position_controller/command'
        
        self.pub = rospy.Publisher(jointTopic, Float64, queue_size=10)

        rospy.Subscriber(jointTopic, Float64, self.storeOldVals)
        rospy.Subscriber('joint_data_input', Float64, self.checkNewInputAndPublish)
        rospy.loginfo("Please publish new values on /joint_data_input")

    def storeOldVals(self, data):
        self.oldVals = data.data
        # rospy.loginfo("old value: " + str(self.oldVals))
    
    def checkNewInputAndPublish(self, data):
        newData = data.data
        if (newData != None):
            if self.oldVals == None:
                rospy.loginfo("Initialising joint value to " + str(newData))
                self.pub.publish(newData)
            else:
                if (newData > self.oldVals):
                    rospy.loginfo("Increasing joint value to " + str(newData))
                    self.pub.publish(newData)

def main():
    jointValue = 1
    # Init ROS node
    rospy.init_node('jointControllerIncrementer', anonymous=True)
    jointControllerIncrementer = JointControllerIncrementer(jointValue)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo('shutting down')

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
