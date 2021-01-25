#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Vector3

class Follower:

        def __init__(self):
                self.lidar_sub = rospy.Subscriber('/scan',
                        LaserScan, self.lidar_check)

                self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)



        def move(self, pos, rot):
                self.cmd_pub.publish(pos, rot)


        def lidar_check(self, msg):

                # To get exact distance from side, multiply by sin(angle)
                IDEAL_DISTANCE = 1.5

                # Check lidar scan 360-30 degrees from front.
                distance = msg.ranges[330]

                # Limit the maximum range to avoid complications.
                if (distance > msg.range_max):
                    distance = msg.range_max

                # Proportional control.

                error = IDEAL_DISTANCE - distance
                        
                Kp = 0.6/distance
                p_out = Kp * error
                self.move(Vector3(0.2, 0, 0,), Vector3(0, 0, p_out))



        def run(self):
                rospy.spin()
                
if __name__ == '__main__':

        rospy.init_node('wall_follower')
        follower = Follower()
        follower.run()
