#!/usr/bin/python
import serial
locations=['/dev/ttyACM0', '/dev/ttyACM2', '/dev/ttyACM3','/dev/ttyACM4', '/dev/ttyACM5','/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3', '/dev/ttyUSB4', '/dev/ttyUSB5', '/dev/ttyUSB6', '/dev/ttyUSB7', '/dev/ttyUSB8', '/dev/ttyUSB9', '/dev/ttyUSB10', 'com2', 'com3', 'com4', 'com5', 'com6', 'com7', 'com8', 'com9', 'com10', 'com11', 'com12', 'com13', 'com14', 'com15', 'com16', 'com17', 'com18', 'com19', 'com20', 'com21', 'com1', 'end']
for device in locations:
   try:
      #print "Trying...",device
      serialport = serial.Serial(device, 2400, timeout = 0)
      print device
      break
   except:
      #print "Failed to connect on",device
      if device == 'end':
         print "Unable to find Serial Port, Please plug in cable or check cable connections."
         exit()
