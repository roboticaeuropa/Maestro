#!/usr/bin/python

import time
import maestro as m

speed=10
#left_fw_speed=6500
#right_fw_speed=5500

s=m.Controller()
s.setTargetA(4,5850,speed,1)
s.setTargetA(5,5850,speed,-1)

time.sleep(2)

s.setTarget(4,0)
s.setTarget(5,0)

