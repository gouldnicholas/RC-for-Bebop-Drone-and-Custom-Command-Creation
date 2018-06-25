#this creates a client that can issue commands to the server without hitting enter
import msvcrt
import sys
from socket import *
#server ip and port can be changed to whatever
serverName = '172.20.10.5'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence= ''
while (sentence !='q')
	print('\n Input Command: ')
	sentence =msvcrt.getche()
	clientSocket.send(sentence)
	modifiedSentence = clientSocket.recv(1024)
	print ('From Server: ', modifiedSentence)
raw_input()
clientSocket.close()