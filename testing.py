# Imports
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import time

# Handlener ->  what to do when you receive data
def listenerHandler(msg):
    print("I am in the listener callback")
    print("Data is ", msg.pose.pose.position.x)
    time.sleep(1)

#startup stuff
rclpy.init()

#make a listner typ enode object
listenerNode = Node("listener")
velocityPublisherNode = Node("listener")

#topic / folder to look in for info
topicName = "/odom"
Velocity_topic = "/cmd_vel"

#initialize
listenerNode.create_subscription(Odometry, topicName, listenerHandler, 10)
velocityPublisher = velocityPublisherNode.create_publisher(Twist, Velocity_topic, 20)

#runs / executes it
#rclpy.spin(listenerNode)
velMsg = Twist()
while True:
    velMsg.linear.x = 1.0
    velMsg.angular.z = 1.0

    velocityPublisher.publish(velMsg)

    time.sleep(1)