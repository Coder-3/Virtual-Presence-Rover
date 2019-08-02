# Virtual Presence Rover
The Virtual Presence Rover is a device which can be driven over LAN with a web interface and live embedded camera feed.
## Connection Instructions

![Connections Graph](https://i.imgur.com/Hz8cS62.png)
![DC Motor Controller to RPi](https://i.imgur.com/t5OJf3L.jpg)
![DC Motor Controller to DC Motors](https://i.imgur.com/jytxB49.jpg)
![RPi to Power](https://i.imgur.com/rgCqo0K.jpg)

## Installation Instructions
1. Connect all modules as seen in the connection diagrams above.
2. Run the following in the Terminal:
	>*sudo apt-get install rpi-update*
	
	>*sudo rpi-update*
	
	>*sudo apt-get update*
	
	>*sudo apt-get install motion*
	
	>*sudo nano /etc/default/motion*
	
3. Locate the following lines and amend with the below:
	>*start_motion_daemon=yes*
	
	>*width 600*
	
	>*heigh 400*
	
	>*framerate 10*
	
	>*stream_localhost off*
	
	>*webcontrol_localhost off*
	
4. Reboot Raspberry Pi
5. >*ifconfig*
6. Copy localhost IP
7. Open *index.html* in the templates folder
8. Replace src=192.168.**xxx** with your own IP.
9. >*sudo motion service start*
10. Run *app.py*
11. Navigate to http://localhost/8000 (replace localhost with the IP you identified in *ifconfig* on a computer connected to the same network as the Raspberry Pi
