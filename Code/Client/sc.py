import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = 'localhost'
port = 8888

# Bind the socket to the host and port
sock.bind((host, port))

# Listen for incoming connections
sock.listen(1)

print("Waiting for a connection...")

# Accept a connection
conn, addr = sock.accept()
print("Connected!")

# Receive and process data
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Received: {data}")

    # Process the received data (e.g., perform some task)

# Close the connection and the socket
conn.close()
sock.close()
