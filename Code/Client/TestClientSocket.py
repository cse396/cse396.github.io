import socket

def connect_to_server():
    # IP address and port for the server socket
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 8002

    # Create a new socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))
        print("Client connected to the server.")

        # Receive and print data from the server
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                print("Received data:", data)
            else:
                break

    except Exception as e:
        print("Error occurred:", e)

    finally:
        # Close the socket connection
        client_socket.close()
        print("Client socket closed.")


if __name__ == "__main__":
    connect_to_server()
