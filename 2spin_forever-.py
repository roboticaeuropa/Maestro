#!/usr/bin/python

import time
import maestro as m
s= m.Controller()

wait_time = 0.35 # In the beginning 0.35

while (1):
	s.setTarget(4,-1)
        s.setTarget(5,-1)
        time.sleep(2)

        s.setTarget(4,0)
        s.setTarget(5,0)
        time.sleep(wait_time)

        s.setTarget(4,1)
        s.setTarget(5,1)
        time.sleep(2)

        s.setTarget(4,0)
        s.setTarget(5,0)
        time.sleep(wait_time)
