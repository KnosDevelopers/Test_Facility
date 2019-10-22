#Testing a simple implementation of Client program

import socket

host = "192.168.18.89" #the local IP of the server
port = 2030 #the same port of the server

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    try:
        print("Initiating connection to the server at ",host)
        server.connect((host,port))
        print("\nEstabilished connection")
    except:
        print("\nCan\'t connect due to some error")

    print("\nSend data to the server to listen its echo.")

    while True:
        usr_data = input("\nEnter data: ")
        echo_heard = False

        while echo_heard == False:
            try:
                print("\nSending data to ",host)
                server.send(byte(usr_data.encode()))
            except:
                print("\nThere was a problem in sending data to the server")

            try:
                data_recv = server.recv(1024)
                print("\nEcho: ",data_recv.decode())
                echo_heard = True
            except:
                print("\nThere was a problem in receiving data from server")
                echo_heard = False
