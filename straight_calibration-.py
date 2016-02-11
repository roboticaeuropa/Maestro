#!/usr/bin/python

import time
import maestro as m
s= m.Controller()

zero=6000
speed=1000

miles   = 0.05  # Positive when left motor runs slower

desv= int(round(speed*miles,0))
print "desv=",desv

speed_left=zero+speed+desv
speed_right=zero-(speed-desv)
print "speed_left",speed_left
print "speed_right",speed_right


s.setTarget(4,speed_left)  #, 1)
s.setTarget(5,speed_right) #,-1)

time.sleep(10)

s.setTarget(4,0)
s.setTarget(5,0)

