#!/usr/bin/python
from sense_hat import SenseHat
import os

sense = SenseHat()
temp = sense.get_temperature()
t = os.popen('/opt/vc/bin/vcgencmd measure_temp')
cputemp = t.read()
cputemp = cputemp.replace('temp=','')
cputemp = cputemp.replace('\'C\n','')
cputemp = float(cputemp)
newtemp = temp - ((cputemp - temp) / 2)
print("%.1f C" % newtemp)



# Return CPU temperature as a character string                                      
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# CPU informatiom
CPU_temp = getCPUtemperature()
# CPU_usage = getCPUuse()

print CPU_temp
