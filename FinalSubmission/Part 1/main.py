import socket
import time

# Create a UDP server socket
server_name = "Adam Nassan"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 8855))
clients = {}# Dictionary to store information about connected clients

try:
    counter = 1# Initialize a counter for assigning client IDs
    print(f"{server_name} is running")
    while True:
        data, address = server_socket.recvfrom(1024)
        client_name = data.decode() # Decode the received data to get the client's name
        if address not in clients:# Check if the client is already in the dictionary
            # If not, add the client to the dictionary
            clients[address] = {'name': client_name, 'last_time': None, 'id': counter}
            counter += 1
        clients[address]['last_time'] =  time.time() # Update the last received time for the client

        print(f"Received message from User {clients[address]['id']}: {clients[address]['name']} at {time.ctime(clients[address]['last_time'])}")
        print("______________________________________________________")
except KeyboardInterrupt:
    print("Program terminated.")