# rpi-nagios

A full Nagios Core installation with environmental monitoring on Raspbian
NagiosGraph for historical data

Requirements are:
Raspberry Pi 3
Sense Hat
Minimum 8GB SD-Card

# Version 1.6.1127

Please download initial img from https://fulhack.io/rpi-nagios.img

INSTALLATION
Download and dd the image file, the Raspberry is configured for dhcp.
SSH pi/raspberry
Nagios installed and browsable at http://<ip>/nagios nagiosadmin/nagiosadmin

CHANGELOG

1.6.1127
- fixed bug with nagiosgraph
- removing retention.dat
- .bash_history was left

1.6.1126
- Upgraded to Nagios Core to v4.2.3
- Added git tools
- Added Ntopng
- Added Nprobe
- Removed sflow-rt
