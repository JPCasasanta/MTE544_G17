# Imports
import rclpy

from rclpy.node import Node

from utilities import Logger, euler_from_quaternion
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

# TODO Part 3: Import message types needed: 
    # For sending velocity commands to the robot: Twist
    # For the sensors: Imu, LaserScan, and Odometry
# Check the online documentation to fill in the lines below
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

from rclpy.time import Time

# You may add any other imports you may need/want to use below
# import ...
import numpy as np


CIRCLE=0; SPIRAL=1; ACC_LINE=2
motion_types=['circle', 'spiral', 'line']

class motion_executioner(Node):

    def __init__(self, motion_type=0):
        
        super().__init__("motion_types") #makes a Node object
        self.speed_inc = 0.0

        self.type=motion_type
        
        self.radius_=0.0
        
        self.successful_init=False
        self.imu_initialized=False
        self.odom_initialized=False
        self.laser_initialized=False
        
        # TODO Part 3: Create a publisher to send velocity commands by setting the proper parameters in (...)
        self.vel_publisher=self.create_publisher(Twist, "/cmd_vel", 10) # arbitrary 10
                
        # loggers
        self.imu_logger=Logger('imu_content_'+str(motion_types[motion_type])+'.csv', headers=["acc_x", "acc_y", "angular_z", "stamp"])
        self.odom_logger=Logger('odom_content_'+str(motion_types[motion_type])+'.csv', headers=["x","y","th", "stamp"])
        self.laser_logger=Logger('laser_content_'+str(motion_types[motion_type])+'.csv', headers=["ranges", "stamp"])
        
        # TODO Part 3: Create the QoS profile by setting the proper parameters in (...)
        #"""  Reliability: RELIABLE
        #History (Depth): UNKNOWN
        #Durability: VOLATILE """
        
        qos=QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT, durability=DurabilityPolicy.VOLATILE, depth=10)

        # TODO Part 5: Create below the subscription to the topics corresponding to the respective sensors
        # ENOCODER subscription
        self.create_subscription(Odometry, "/odom", self.odom_callback, qos)
        
        
        # IMU subscription
        self.create_subscription(Imu, "/imu", self.imu_callback, qos)
        #...
        
        # LaserScan subscription 
        self.create_subscription(LaserScan, "/scan", self.laser_callback, qos)
        #...
        
        self.create_timer(0.1, self.timer_callback)


    # TODO Part 5: Callback functions: complete the callback functions of the three sensors to log the proper data.
    # You can save the needed fields into a list, and pass the list to the log_values function in utilities.py
    
    #log imu msgs
    def imu_callback(self, imu_msg: Imu):
        imu_list = [imu_msg.linear_acceleration.x, imu_msg.linear_acceleration.y, imu_msg.angular_velocity.z, Time.from_msg(imu_msg.header.stamp).nanoseconds]
        self.imu_logger.log_values(imu_list)
        
    # log odom msgs
    def odom_callback(self, odom_msg: Odometry):
        yaw = euler_from_quaternion(odom_msg.pose.pose.orientation)
        odom_list = [odom_msg.pose.pose.position.x, odom_msg.pose.pose.position.y, yaw, Time.from_msg(odom_msg.header.stamp).nanoseconds]
        self.odom_logger.log_values(odom_list)
                
    # log laser msgs with position msg at that time
    def laser_callback(self, laser_msg: LaserScan):
        #convert to python array
        laser_ranges = laser_msg.ranges.tolist()

        laser_list = [laser_msg.angle_min, laser_msg.angle_max, laser_msg.angle_increment, laser_msg.range_min, laser_msg.range_max, Time.from_msg(laser_msg.header.stamp).nanoseconds]
        laser_list.extend(laser_ranges)
        self.laser_logger.log_values(laser_list)
                
    def timer_callback(self):
        
        '''
        print("in timer callback")

        if self.odom_initialized and self.laser_initialized and self.imu_initialized:
            self.successful_init=True
            
        if not self.successful_init:
            return
        
        print("in timer callback")
        '''

        cmd_vel_msg=Twist()
        
        if self.type==CIRCLE:
            cmd_vel_msg=self.make_circular_twist()
        
        elif self.type==SPIRAL:
            cmd_vel_msg=self.make_spiral_twist()
                        
        elif self.type==ACC_LINE:
            cmd_vel_msg=self.make_acc_line_twist()
            
        else:
            print("type not set successfully, 0: CIRCLE 1: SPIRAL and 2: ACCELERATED LINE")
            raise SystemExit 

        self.vel_publisher.publish(cmd_vel_msg)
        
    
    # TODO Part 4: Motion functions: complete the functions to generate the proper messages corresponding to the desired motions of the robot

    def make_circular_twist(self):
        print("making a circle")
        msg=Twist()
        msg.linear.x = 0.75
        msg.angular.z = 2.0
        # fill up the twist msg for circular motion
        return msg

    def make_spiral_twist(self):
        msg=Twist()
        msg.linear.x = 0.0 + self.speed_inc
        if (self.speed_inc < 2.5):
            self.speed_inc = self.speed_inc + 0.01
        msg.angular.z = 2.0
        # fill up the twist msg for spiral motion
        return msg
    
    def make_acc_line_twist(self):
        msg=Twist()
        msg.linear.x = 0.0 + self.speed_inc
        if (self.speed_inc < 69):
            self.speed_inc = self.speed_inc + 0.01
        msg.angular.z = 0.0
         # fill up the twist msg for line motion
        return msg

import argparse

if __name__=="__main__":
    

    argParser=argparse.ArgumentParser(description="input the motion type")


    argParser.add_argument("--motion", type=str, default="circle")



    rclpy.init()

    args = argParser.parse_args()

    if args.motion.lower() == "circle":
        #Create the object
        print("input was a circle")
        ME=motion_executioner(motion_type=CIRCLE)
    elif args.motion.lower() == "line":
        ME=motion_executioner(motion_type=ACC_LINE)

    elif args.motion.lower() =="spiral":
        ME=motion_executioner(motion_type=SPIRAL)

    else:
        print(f"we don't have {args.motion.lower()} motion type")


    
    try:
        #Start running th eobject
        rclpy.spin(ME)
    except KeyboardInterrupt:
        print("Exiting")
