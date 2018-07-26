# IP Configuration on Ubuntu side for ATI FT Sensors, WSG Gripper, and ABB IRB Robots

Steps:

## 1. Using Ethernet-to-USB adaptors, plug in the devices into your machine.

Make sure the machine is not trying to connect to the devices.

## 2. Go to the connections icon in the top right, and go to edit connections.
## 3. Create a new ethernet connection and name it.
## 4. In Ethernet tab, in device MAC address, select the ethernet connection desired.
## 5. In IPv4 tab:

Note the IP address of the device, if there are multiple devices with a single Ethernet cable, 
you'll need all the IP addresse.

Enter the first 3 numbers of the IP address, and for the last number enter anything but the matching
IP of the device, i.e. if the device is `192.168.37.3`, you enter `192.168.37.10`.

2nd tab - In the Mask, use `255.255.255.0`.

3rd tab - In the Gateway, enter 0.0.0.0

## 6. Connect to the devices and ping to make sure
