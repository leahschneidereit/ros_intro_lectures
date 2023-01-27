#!/usr/bin/env python3

#import ROS for developing the node
import rospy

#import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	#declare publisher 
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	#initialize the node
	rospy.init_node('vel_publisher_node', anonymous = True)
	#set frequency for loop
	loop_rate = rospy.Rate(10)
	#declare variable of type twist for sending commands
	vel_cmd = Twist()
	# run this control loop regularly 
	while not rospy.is_shutdown():
		#set linear (forward/backward) velocity command
		vel_cmd.linear.x = 0.5
		#set angular velocity command
		vel_cmd.angular.z = 0.5
		#publish command to defined topic
		cmd_pub.publish(vel_cmd)
		#wait for 0.2 seconds until the next loop and repeat
		loop_rate.sleep()
