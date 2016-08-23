import serial
import time

class ServoController:
    def __init__(self):
        usbPort = '/dev/ttyACM0'
        
        self.sc = serial.Serial(usbPort, timeout=1)
        # Command lead-in and device 12 are sent for each Pololu serial commands.
        self.PololuCmd = chr(0xaa) + chr(0xc)
        self.Targets = [0] * 24
        # Servo minimum and maximum targets can be restricted to protect components.
        self.Mins = [0] * 24
        self.Maxs = [0] * 24

    def closeServo(self):
        self.sc.close()

    def setRange(self, chan, min, max):
        self.Mins[chan] = min
        self.Maxs[chan] = max
        

    def setAngle(self, n, angle):
        if angle > 360 or angle <0:
           angle=90
        byteone=int(512*angle/360)
        
        bud=chr(0xFF)+chr(n)+chr(byteone)
        self.sc.write(bud)
        
    def setAngulo(self, n, angle,angle2):
        byteone=int(angle)
        bytetwo=int(254*angle2/180)
        bud=chr(0xFF)+chr(n)+chr(byteone)+chr(bytetwo)
        self.sc.write(bud)


    def setPosition(self, servo, position):
        position = position * 4
        poslo = (position & 0x7f)
        poshi = (position >> 7) & 0x7f
        chan  = servo &0x7f
        data =  chr(0xaa) + chr(0x0c) + chr(0x04) + chr(chan) + chr(poslo) + chr(poshi)
        self.sc.write(data)

    def getPosition(self, servo):
        chan  = servo &0x7f
        data =  chr(0xaa) + chr(0x0c) + chr(0x10) + chr(chan)
        self.sc.write(data)
        w1 = ord(self.sc.read())
        w2 = ord(self.sc.read())
        return w1, w2

    def getPosition2(self, chan):
        cmd = self.PololuCmd + chr(0x10) + chr(chan)
        self.sc.write(cmd)
        lsb = ord(self.sc.read())
        msb = ord(self.sc.read())
        return (msb << 8) + lsb

    def getErrors(self):
        data =  chr(0xaa) + chr(0x0c) + chr(0x21)
        self.sc.write(data)
        w1 = ord(self.sc.read())
        w2 = ord(self.sc.read())
        return w1, w2

    def triggerScript(self, subNumber):
        data =  chr(0xaa) + chr(0x0c) + chr(0x27) + chr(0)
        self.sc.write(data)

    def setTarget(self, chan, target):

        target = target * 4
        lsb = target & 0x7f #7 bits for least significant byte
        msb = (target >> 7) & 0x7f #shift 7 and take next 7 bits for msb
        # Send Pololu intro, device number, command, channel, and target lsb/msb
        cmd = self.PololuCmd + chr(0x04) + chr(chan) + chr(lsb) + chr(msb)
        self.sc.write(cmd)

    def setSpeed(self, chan, speed):
        
        lsb = speed & 0x7f #7 bits for least significant byte
        msb = (speed >> 7) & 0x7f #shift 7 and take next 7 bits for msb
        # Send Pololu intro, device number, command, channel, speed lsb, speed msb
        cmd = self.PololuCmd + chr(0x07) + chr(chan) + chr(lsb) + chr(msb)
        self.sc.write(cmd)
        
        
