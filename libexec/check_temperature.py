#!/usr/bin/python2.7

import os
import sys
from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()
t = os.popen('/opt/vc/bin/vcgencmd measure_temp')
cputemp = t.read()
cputemp = cputemp.replace('temp=','')
cputemp = cputemp.replace('\'C\n','')
cputemp = float(cputemp)
newtemp = temp - ((cputemp - temp) / 1.3)
#print("%.1f C" % newtemp)
#print cputemp
#print temp

newtemp = int(newtemp)
red = (255, 0, 0)
green = (0, 255, 0)

sense.clear()

if newtemp > 35:
    print "Temperature is too high!, currently", newtemp, "degrees Celsius", "| temp=" + str(newtemp) + ";35;40"
    sense.show_message(newtemp, text_colour=red)
    sense.load_image("/usr/local/nagios/libexec/rainbow.png")
    sys.exit(2) 

print "Temperature is OK!, currently", newtemp, "degrees Celsius","| temp=" + str(newtemp) + ";35;40"
newtemp = str(newtemp)
sense.show_message(newtemp, text_colour=green)
sense.low_light = True
sense.load_image("/usr/local/nagios/libexec/rainbow.png")
sys.exit(0)
