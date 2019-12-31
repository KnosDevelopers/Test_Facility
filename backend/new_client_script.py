#Testing a simple implementation of Client program

import socket

host = "0.tcp.ngrok.io" #the local IP of the server
port = 16617 #the same port of the server

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    print("\nInitiating connection to the server")
    server.connect((host,port)) 
    print("Connected to the server at",host)
except:
    print("\nCan\'t connect due to some error")
    quit()

print("\nSend data to the server to listen its echo.")

while True:
    data = str(input("\nType something: "))
    server.send(data.encode('ascii'))
    data_recv = server.recv(1024)
    print("Received from server : ",str(data_recv.decode('ascii')))
    ans = input("\nDo you want to continue? (y/n)")
    if ans=='y':
        continue
    else:
        break
server.close()