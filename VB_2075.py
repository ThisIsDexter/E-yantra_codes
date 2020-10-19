#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt

class turtlebot():

    def __init__(self):
        
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(50)


    def callback(self, data):
        self.pose = data
        self.pose.theta = round(self.pose.theta, 4)
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def make_circle(self):

        r = 1 # radius
        f = 1 # frequency
        n = 1.2 # turns for future tests


        goal_pose = Pose()
        vel_msg = Twist()
        self.rate.sleep()
        t0 = float(rospy.Time.now().to_sec())
        distance = 0

        angle = self.pose.theta

        while (2*3.1416*r*n) >= distance:
            vel_msg.linear.x = 2*3.1416*f*r
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

                #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 2*3.1416*f
            print(self.pose.x)
            t1=float(rospy.Time.now().to_sec())
            distance = vel_msg.linear.x * (t1-t0)
            print('No. of turns = '+ str( distance/(2*3.1416*r)))



            self.velocity_publisher.publish(vel_msg) #Publishing our vel_msg
            self.rate.sleep()
        #stopping it
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)
        print(distance//(2*3.1416*r))


if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.make_circle()
    except rospy.ROSInterruptException:
        pass
