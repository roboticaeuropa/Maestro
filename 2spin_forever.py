#!/usr/bin/python

import time
import maestro as m
s= m.Controller()

while (1):
    for i in range(1,3):
        s.setTarget(4,-1)
        s.setTarget(5,1)
        time.sleep(5)

        s.setTarget(4,0)
        s.setTarget(5,0)
        time.sleep(1)

        s.setTarget(4,1)
        s.setTarget(5,-1)
        time.sleep(5)

        s.setTarget(4,0)
        s.setTarget(5,0)
        time.sleep(1)
