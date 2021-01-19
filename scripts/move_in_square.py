#!/usr/bin/env python3
""" This script sends velocity commands to a robot, causing it to move in a square-pattern. """
import rospy

from geometry_msgs.msg import Twist, Vector3#, PoseWithCovariance, Pose, Quaternion, TwistWithCovariance
#from nav_msgs.msg import Odometry
from math import pi






class ROS:


   

    def __init__(self):
        rospy.init_node('move_in_square')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        #self.sub = rospy.Subscriber('/odom', Odometry, self.check_turn)  
        #self.turn_angle = 0

    #def check_turn(self, data):
        #self.turn_angle = data.pose.pose.orientation.z
        #print (self.turn_angle)

    def move(self, pos, rot):
        self.pub.publish(pos, rot)


    def run(self):
        r = rospy.Rate(10)
        zero_pos = Vector3(0,0,0)
        zero_rot = Vector3(0,0,0)
        self.move(zero_pos, zero_rot)
        #The system seems to take some time to load in gazebo, so I added a wait.
        rospy.sleep(10)
        while not rospy.is_shutdown():
            self.move(Vector3(0.3,0,0), zero_rot)
            rospy.sleep(4) 
            #self.move(zero_pos, zero_pos)
            #rospy.sleep(1)
            #rotate Pi/2 radians in 4 seconds.
            self.move(Vector3(0.3,0,0), Vector3(0,0,pi/8))
            rospy.sleep(4)
            


if (__name__ == '__main__'):
    robot = ROS()
    robot.run();

