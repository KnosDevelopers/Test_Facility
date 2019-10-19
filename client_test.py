#Testing a simple implementation of Client program

import socket

host = "192.168.18.68" #the local IP of the server
port = 2030 #the same port of the server

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    
    print("Trying to estabilish connection with the server...")
   
    server.connect((host,port)) #trying to connect
    server.send(b"Master")
    data = server.recv(1024)

    if data == b"Permission Granted":
        print("Connection estabilished successfully to server")
    else:
        print(data)