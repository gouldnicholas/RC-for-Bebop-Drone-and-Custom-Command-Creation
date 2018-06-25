
#imports all the necessary libraries
from socket import *
import sys
import os
import code
import readline
import rlcompleter
sys.path.append('../src')
import Bybop_Device
from Bybop_Discovery import *

#searches for and connects to Drone. If it cant connect it will close out of the program
print 'Searching for devices'
discovery = Discovery(DeviceID.ALL)
discovery.wait_for_change()
devices = discovery.get_devices()
discovery.stop()
if not devices:
    print 'Oops ...'
    sys.exit(1)
device = devices.itervalues().next()
print 'Will connect to ' + get_name(device)
d2c_port = 54321
controller_type = "PC"
controller_name = "bybop shell"
drone = Bybop_Device.create_and_connect(device, d2c_port, controller_type, controller_name)
if drone is None:
    print 'Unable to connect to a product'
    sys.exit(1)
drone.dump_state()

#the server can now accept commands from the client and send to the drone
print str('The server is ready to receive')
#creates server
serverSocket = socket(AF_INET,SOCK_STREAM)
serverPort = 12000#port and IP can be changed to whatever
serverSocket.bind(('172.20.10.5',serverPort))
serverSocket.listen(1)



#command loop
while 1:
	#accepts connection from client
	client,addr=serverSocket.accept()
	data = client.recv(2048)
	print("Recieved ",data," from client\n")
	print("Processing\n")
	#commands. data can be changed to any button.
	if (data =="t"):
		client.send("take off")
		print(" take off\n")
		drone.take_off()
	elif (data == "h"):
		client.send("hover")
		drone.take_off()
		print(" hover\n")
	elif (data == "o"):
		client.send("land")
		print(" land\n")
		drone.land()
	elif (data == "l"):
		client.send("left roll")
		print(" left roll\n")
		drone.left()
	elif (data == "r"):
		client.send("right roll")
		print(" right roll\n")
		drone.right()
	elif (data == "f"):
		client.send("front tilt")
		print(" front tilt\n")
		drone.forward()
	elif (data == "b"):
		client.send("b")
		print(" back tilt\n")
		drone.back()
	elif (data == "1"):
		client.send("upwards vertical speed")
		print(" upwards vertical speed\n")
		drone.rise()
	elif (data == "2"):
		client.send("downwards vertical speed")
		print("downwards vertical speed\n")
		drone.lower()
	elif (data == "3"):
		client.send("rotate left")
		print(" rotate left\n")
		drone.rleft()
	elif (data == "4"):
		client.send("rotate right")
		print(" rotate right\n")
		drone.rright()
	elif (data == "e"):
		client.send("emergency shutoff")
		print("emergency shutoff")
		drone.emergency()
	elif (data == "close"):
		client.send("closing")
		drone.land()
		drone.emergency()
		drone.stop()
		client.close()
		break
	else:
		client.send("wrong command")
		print("wrong command\n")

