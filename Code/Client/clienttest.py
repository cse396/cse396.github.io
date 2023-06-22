import socket
import ast
import time

# Socket setup
HOST = 'localhost'  # Replace with the appropriate host IP address
PORT = 9003  # Replace with the appropriate port number
BUFFER_SIZE = 1024
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
input_stream = client_socket.makefile("r")
output_stream = client_socket.makefile("w")

def send_map_data(map_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data_str = str(map_data)
            s.sendall(data_str.encode())  # Send the map data as bytes
            ack = s.recv(BUFFER_SIZE).decode()  # Receive acknowledgment from the server
            print("Server acknowledgment:", ack)
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running and accepting connections.")
    except Exception as e:
        print("An error occurred while sending map data:", str(e))


while True:
    # Sample map data
    map_data = {
        'degree': 90,
        'sonic1': 10,
        'sonic2': 4.5
    }
    
    print("Connected to server", client_socket.getpeername())

    # create input and output streams for the socket
    send_map_data(map_data)

    # Wait for some time before sending the next map data
    time.sleep(1)
