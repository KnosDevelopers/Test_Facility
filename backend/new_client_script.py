#Testing a simple implementation of Client program

import socket
import smtplib
import pymongo

def main(port_no):
    host = "0.tcp.ngrok.io" #the local IP of the server
    port = int(port_no) #the same port of the server
    print("Using PORT ", port)

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
        first_name = str(input("\nType First Name: "))
        last_name = str(input("\nType Last Name: "))
        user_name = str(input("\nType User Name: "))
        email = str(input("\nType Email: "))
        password = str(input("\nType Password: "))
        country = str(input("\nType Country: "))
        data = ('ts'+':'+first_name+':'+last_name+':'+user_name+':'+email+':'+password+':'+country)
        server.send(data.encode('ascii'))
        data_recv = server.recv(1024)
        print("Received from server : ",str(data_recv.decode('ascii')))
        ans = input("\nDo you want to continue? (y/n)")
        if ans=='y':
            continue
        else:
            break
    server.close()

def port_checker():
    
    client = pymongo.MongoClient("mongodb+srv://portmaster:freehitportmaster@testacoda-001-cj5sj.mongodb.net/test?retryWrites=true&w=majority")
    db = client.freehit_db
    collection = db.port
    cursor = collection.find({})
    for document in cursor:
        port_no = document['port']
    
    return port_no
    
main(port_checker())