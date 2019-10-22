#Testing a simple implementation of Client program

import socket

host = "192.168.18.89" #the local IP of the server
port = 2030 #the same port of the server

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    try:
        print("\nInitiating connection to the server")
        server.connect((host,port)) 
        print("Connected to the server at",host)
    except:
        print("\nCan\'t connect due to some error")
        quit()

    print("\nSend data to the server to listen its echo.")

    while True:
        usr_data = input("\nEnter data: ")
        echo_heard = False

        while echo_heard == False:
            
            print("\nSending data to server at",host)
            server.sendall(bytes(usr_data.encode()))
            
            try:
                data_recv = server.recv(1024)
                print("\nEcho: ",repr(data_recv))
                echo_heard = True
            except:
                print("\nThere was a problem in receiving data from server")
                echo_heard = False
            finally:
                break
        
