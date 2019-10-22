# Testing a simple implementation of listening server.

import socket

host = '192.168.18.89' #local IPV4 address of the machine
port = 2030 #any port above the range of 1020

print("\nRunning...")

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((host,port))
    print("\nServer estabilished. Waiting for connections")
    server.listen()
    connection,address = server.accept()
    print("\nConnection estabilished to client at ",address)

    while True:
        received = False

        while received == False:
            try:
                print("\nWaiting for data from client at ",address)
                data = connection.recv(1024)
                received = True
            except:
                print("\nSome error occured while receiving data from client at ",address)
                received = False
            finally:
                continue
        print("\nReceived data: ",data.decode())
        
        echoed = False
        while echoed == False:
            try:
                connection.send(data.encode())
                print("\nEchoed data: ",data.decode())
                echoed = True
            except:
                print("Some error occured while echoeing back to client at ",address)
                echoed = False
            finally:
                continue

