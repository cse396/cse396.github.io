import socket
import time
import json

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = 'localhost'
port = 9000

# Connect to the server
sock.connect((host, port))


map_data = {
    'degree': 90,
    'sonic1': 30,
    'sonic2': 20
}

# send this data in a loop
for i in range(100):

    # increment the degree by 10
    map_data['degree'] += 10

    # increment the sonic1 by 1
    map_data['sonic1'] += 15
    map_data['sonic2'] += 10

    print(map_data)

    json_str = json.dumps(map_data)

    encoded_data = json_str.encode()

    sock.sendall(encoded_data)

    time.sleep(1)


# Close the socket
sock.close()
