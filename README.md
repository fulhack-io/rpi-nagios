# rpi-nagios

A full Nagios Core installation with environmental monitoring on Raspbian.
Using PNP4Nagios and Grafana for performance data.

Requirements for Nagios Core are:
Raspberry Pi 3
8GB SD-Card

For Temperature and Humidity checks:
Sense Hat

# Version 1.6.1127

Please download initial img from https://fulhack.io/rpi-nagios.img

INSTALLATION
Download and use etcher or similar tool for flashing the image file.

The Raspberry is configured for dhcp on eth0, if there is no ip address on eth0 a timed check will start the Wifi in AP mode and Broadcast the SSID "NagiosCore". The key for this SSID is also "NagiosCore"
The check will run continuusly, if it detects an IP on eth0 it will stop broadcasting the Wifi.

SSH access: pi/raspberry
Nagios Access at http://<dhcp-ip>/nagios or if running in AP mode http://10.223.223.1/nagios with nagiosadmin/nagiosadmin as credentials

The performance data is being sampled to both PNP4Nagios and InfluxDB via NagFlux. Grafana is configured to read the performance data from InfluxDB. Both are reachable directly from the host or service via the small icons. PNP4Nagios will open in the main window and all other graphs attatched to the same host will be visable. The Grafana button will open in a separate tab/window over port 3000 and the button have pre-configured Histou/InfluxDB queries.

Grafana access: admin/admin

When running in AP mode the Histou and notes_url will work out of the box, when running on dhcp or static IP three things needs to change:




CHANGELOG

1.9.0619
- Removed NagiosGraph 
- Removed NTOP
- Added PNP4Nagios
- Added InfluxDB
- Added Grafana
- Added Nagflux
- Added Histou
- Added AP Mode if eth0 is not connected
- upgraded to Nagios Core 4.4.3
- Added Golang
- Changed Check interval on Humidity/Temperature to every minute
- Fixed a bug in the Humidity check


1.6.1127
- fixed bug with nagiosgraph
- removing retention.dat
- .bash_history was left

1.6.1126
- Upgraded to Nagios Core 4.2.3
- Added git tools
- Added Ntopng
- Added Nprobe
- Removed sflow-rt
