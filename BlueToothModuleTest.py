import sys
import serial
import atexit
import time

class command(object):
    def __init__(self):
        self.play = 'MA'
        self.next = 'MD'
        self.last = 'ME'

        self.call = 'CI'
        self.volup = 'VU'
        self.voldo = 'VD'

        self.answer = 'CE'
        self.reject = 'CF'
        self.endcall = 'CG'
        self.redial = 'CH'

        self.connect = 'CC' #anser IV = connected
        self.state_query = 'CY' #answer MGx, x= 1:ready 2:connecting 3:connected 
                                #4:outgoing call 5:incomming call 6:ongoing call


class blue_tooth_module(object):
    def __init__(self, test):
        self.test = test

    def connect(self):
        self.ser = serial.Serial('/dev/ttyACM1', 9600, timeout=2)
        time.sleep(1)

    def send(self, cmd):
        self.ser.write(b'AT#'+cmd+'\r\n') 

    def readline(self):
        self.ser.readline()

def main():
    bl = blue_tooth_module("test")
    bl.connect()

    while True:
        print "please enter your command"
        inp = raw_input()
        bl.send(inp)
        time.sleep(1)
        while True:
            str = bl.readline()
            if str == None:
                break
            else:
                print str



if __name__ == '__main__':
    #atexit.register(exit_handler)
    main()

