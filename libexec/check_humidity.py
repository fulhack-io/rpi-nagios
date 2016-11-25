#!/usr/bin/python2.7

import sys
from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
humidity = int(humidity)

if humidity > 40:
    print "humidity is too high!, currently", humidity, "%| humidity=" + str(humidity) + ";40;45"
    sys.exit(2)

print "humidity is OK!, currently", humidity, "% | humidity=" + str(humidity) + ";40;45"
sys.exit(0)
