# Testing a simple implementation of listening server.

import socket

host = '192.168.18.68' #local IPV4 address of the machine
port = 2030 #any port above the range of 1020

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((host,port))
    server.listen()
    connection,address = server.accept()
    
    print("Server estabilished. Waiting for connections...")

    with connection:
        print("New connection from " + str(address))
        print("\n")

        while True:
            received = False

            while received == False:
                msg = (str(input("Enter message ==> "))).encode()
                connection.send(bytes(msg))
                print("\n")
                msg_recv = connection.recv(1024)
                print(msg_recv.decode(),"\n")
                received = True