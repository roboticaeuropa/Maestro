#!/usr/bin/python

from uart_device import Device
import time
 
#create servo object, set unlimited speed, move servo to 90 degrees angle
servo = Device("/dev/ttyAMA0","/dev/ttyAMA0")
servo.set_speed(0,5)
servo.mid(0)
time.sleep(1)
 
d=0
loop=0
 
#sweeping program
#increase speed in each iteration
while (loop<10):
       speed=5+(loop*15)
       print("Iteration = ", loop, ". Speed = " , speed)
       servo.set_speed(0,speed)
       if(d==0):
               servo.up(0)
               d=1
       else:
               servo.down(0)
               d=0
       time.sleep(2)
       loop=loop+1
