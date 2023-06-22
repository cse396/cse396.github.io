import socket
import time

# get IP address
HOST = socket.gethostbyname(socket.gethostname())

# Port 8002 for sending mapping data
server_socket2 = socket.socket()
server_socket2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket2.bind((HOST, 8002))
server_socket2.listen(1)
print('New socket address:', HOST)
def transmission_mapping():
    try:
        connection2, client_address2 = server_socket2.accept()
        print("New socket connected ... ")
    except:
        print("New socket connect failed")
    server_socket2.close()
    while True:
        try:
            # TODO: hello yerine mapping datasi yollanacak
            connection2.send("hello".encode('utf-8'))
            time.sleep(0.1)
        except Exception as e:
            print(e)
            break
    print("End transmit ... ")
    connection2.close()

transmission_mapping()