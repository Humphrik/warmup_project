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

                # How far away should the robot get?
                IDEAL_DISTANCE = 0.75

                # We need both the minimum range and the angle it occurs.
                current_distance = msg.ranges[0]
                current_angle = 0
                for i in range(0, 360):
                    # Probably not needed, but considers floating point error.
                    if (msg.ranges[i] <= current_distance and msg.ranges[i] >= msg.range_min):
                        current_angle = i
                        current_distance = msg.ranges[i]


                #Set range to max if it is over the maximum.
                if (current_distance > msg.range_max):
                    current_distance = msg.range_max

                #Convert angles over 360 to negative
                if (current_angle > 180):
                    current_angle = current_angle - 360


                print ("The closest object is at angle: ", current_angle)
                print ("It is at distance: ", current_distance)
                #print ("Debug: ", msg.ranges[0])


                # Proportional control for distance
                error_d = current_distance - IDEAL_DISTANCE
                error_a = current_angle
                



               
                Kp_a = (1.0/45)
                Kp_d = 0.8/current_distance


                d_out = Kp_d * error_d
                a_out = Kp_a * error_a

                self.move(Vector3(d_out, 0, 0,), Vector3(0, 0, a_out))



        def run(self):
                rospy.spin()
                
if __name__ == '__main__':

        rospy.init_node('person_follower')
        follower = Follower()
        follower.run()
