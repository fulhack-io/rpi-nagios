# rpi-nagios

A full Nagios Core installation with environmental monitoring on Raspbian.
Using PNP4Nagios and Grafana for performance data.

Requirements for Nagios Core are:
Raspberry Pi 3
8GB SD-Card

For Temperature and Humidity checks:
Sense Hat

Current Version 1.9.0622

Please download initial img from https://fulhack.io/rpi-nagios.img


# INSTALLATION

Download and use etcher or similar tool for flashing the image file.

The Raspberry is configured for dhcp on eth0 and will Broadcast the SSID "NagiosCore" from uap0. The key for this SSID is also "NagiosCore"

Connect to the SSID and open a web browser and browse http://nagioscore/ A RasAP interface will enable you to connect to a separate Wifi with the Raspberry wlan0 and route your computer traffic.

Nagios Access at http://dhcp-ip/nagios or if running in AP mode http://nagioscore/nagios, there is also a link in the RaspAP interface for ease of access. 

SSH access: pi/raspberry
Web access nagiosadmin/nagiosadmin
Grafana access admin/admin

The performance data is being sampled to both PNP4Nagios and InfluxDB via NagFlux. Grafana is configured to read the performance data from InfluxDB. Both are reachable directly from the host or service via the small icons. PNP4Nagios will open in the main window and all other graphs attatched to the same host will be visable. The Grafana button will open in a separate tab/window over port 3000 and the button have pre-configured Histou/InfluxDB queries.

When running in AP mode the Histou and notes_url will work out of the box, when running on dhcp or static IP three things needs to change (or add to local DNS):

In the file /usr/share/grafana/public/dashboards/histou.js, change the "var url = 'http://nagioscore/histou/';" to match your setup.

In the file /usr/local/nagios/etc/objects/templates.cfg, change both (2) the "notes_url  http://nagioscore:3000" to match your setup.

To change timezone, do sudo raspi-config from cli.


CHANGELOG

1.9.0622
- Added RaspAP
- Added uap0

1.9.0619
- Removed NagiosGraph 
- Removed NTOP
- Added PNP4Nagios
- Added InfluxDB
- Added Grafana
- Added Nagflux
- Added Histou
- Added AP Mode if eth0 is not connected
- Added Golang
- upgraded to Nagios Core 4.4.3
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
