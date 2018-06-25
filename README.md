# RC-for-Bebop-Drone-and-Custom-Command-Creation
This is a remote controller for the Bebop Drone via a client and a server. This allows for the drone to be controlled from anywhere with an internet connection. In addition, this  allows the creation of custom commands for the bebop drone.Everything is written in python.

In order for the server to drone communication needs to happen,all of the BYBOP sources created by N-BC need to be downloaded on to the host that is running the server. those can be found here:https://github.com/N-Bz/bybop/tree/master/src. 

In order to create custom commands,open up Custom_Bybop_Device.py in a text editor,scroll down to the BebopDrone class and find the code comments to see how to create custom commands. Essentially copy and paste the function "rise", and change rise to whatever your custom command is going to be called.Once done, there are 6 interger values that can be edited.each integer value represents the following: flag,pitch,roll,yaw,and gaz.(in that order)When flag is set to 0, it locks pitch and roll. Once a custom command has been created make sure to add it in to the list of commands on the server.I added 8 new custom commands to add functionality to the drone.

Now, replace the Bybop_Device.py with Custom_Bybop_Device.py.Once done, either change Custom_Bybop_Device.py back to Bybop_Device.py or go through all of the source files and for every instance a file imports Bybop_Device, replace Bybop_Device with with Custom_Bybop_Device.
