#!/usr/bin/env python3
""" This script receives ROS messages containing the 3D coordinates of a single point and prints them out """
import rospy

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan




class ROS:



    def __init__(self):
        rospy.init_node('stop_at_wall')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.check_wall)


    def check_wall(self, data):
        print ("Distance from forward wall: " + str(data.ranges[0]))
        if(data.ranges[0] < 0.5):
            self.pub.publish(Vector3(0,0,0), Vector3(0,0,0))
        else:
            self.pub.publish(Vector3(0.25,0,0), Vector3(0,0,0))



    def run(self):
        #r = rospy.Rate(2)
        #while not rospy.is_shutdown():
        #    self.pub.publish(Vector3(0,0,0), Vector3(0,0,0))
        #    r.sleep()
        rospy.spin()


if (__name__ == '__main__'):
    robot = ROS()
    robot.run();

