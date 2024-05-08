import time
from socket import *

serverName = "192.168.1.255"#define the server IP address
serverPort = 8855#define the port number
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

student_name = input("Enter your name: ")

try:
    while True:
        message = student_name
        clientSocket.sendto(message.encode(), (serverName, serverPort))#send the encoded message to the server
        time.sleep(2)#delay of 2 seconds
except KeyboardInterrupt:
    print("Program terminated.")

clientSocket.close()