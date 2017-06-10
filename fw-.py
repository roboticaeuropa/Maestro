#!/usr/bin/python

import time
import maestro as m

left_fw_speed=6500
right_fw_speed=5500

s= m.Controller()
s.setTarget(4,left_fw_speed)
s.setTarget(5,right_fw_speed)

time.sleep(2)

s.setTarget(4,0)
s.setTarget(5,0)

