#!/usr/bin/python

import time
import maestro as m
s= m.Controller()

while (1):
	s.setTarget(4,-1)
        s.setTarget(5,1)
        time.sleep(2)

        s.setTarget(4,0)
        s.setTarget(5,0)
        time.sleep(0.35)

        s.setTarget(4,1)
        s.setTarget(5,-1)
        time.sleep(2)

        s.setTarget(4,0)
        s.setTarget(5,0)
        time.sleep(0.35)
