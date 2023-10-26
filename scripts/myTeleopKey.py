#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist 
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from numpy import pi
import termios, sys, os
from turtlesim.msg import Pose
TERMIOS = termios

import sys

import rospy
from geometry_msgs.msg import Twist 
# initialising pygame

def pubVel(vel_x, ang_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.angular.z = ang_z
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

def callback(data):
    rospy.loginfo(data.x)

def pose():
    rospy.init_node('poseSub', anonymous=False)
    rospy.Subscriber("turtle1/pose", Pose, callback)
    print(Pose.x)
    print(Pose.y)
    rospy.spin()

def teleport(x, y, ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(x, y, ang)
        print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))



def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c


tecla="****"
while True:
    tecla=str(getkey())

    if tecla[2]=="a":
        print("se presiono a")
        pubVel(0,0.4,1)
    elif tecla[2]=="d":
        print("se presiono d")
        pubVel(0,-0.4,1)
    elif tecla[2]=="w":
        print("se presiono w")
        pubVel(1,0,1)
    elif tecla[2]=="s":
        print("se presiono s")
        pubVel(-1,0,1)
    elif tecla[2]==" ":
        print("se presiono espacio")
        pubVel(0,pi/2,1)
    elif tecla[2]=="r":
        print("se presiono r")
        teleport(5.544444561004639,5.544444561004639,0)
    
    
