#Testing a simple implementation of Client program

import socket
import smtplib
import pymongo
import re

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
        pass

    print("Testing signup feature...")
    name = str(input("\nName : "))
    flag = False
    while flag==False:
        username = input("\nUsername : ")
        if username_validator(username) == "ErrorCode : ec02":
            print("\nUsername is already taken! Try another one")
            flag = False
        else:
            flag = True
    flag = False
    while flag==False:
        email = input("\nEmail : ")
        if email_validator(email) == "ErrorCode : ec03":
            print("Invalid email or the email is already taken")
            flag = False
        else:
            flag = True
    password = input("\nPassword : ")
    flag = False
    while flag==False:
        retype = input("\nRetype password : ")
        if password_repeater(password,retype) == "ErrorCode : ec04":
            print("Passwords dont match! Retype password")
            flag == False
        else:
            flag = True
    data_string = name+":"+username+":"+email+":"+password
    data_train('op01',data_string,server)
    server.close()

def port_checker():
    client = pymongo.MongoClient("mongodb+srv://port_checker:freehit_portchecker@testacoda-001-cj5sj.mongodb.net/test?retryWrites=true&w=majority")
    db = client.freehit_db
    collection = db.port
    cursor = collection.find({})
    for document in cursor:
        port_no = document['port']
    return port_no

def password_repeater(pswrd,rpswrd):
    if pswrd != rpswrd:
        return("ErrorCode : ec04")
    else:
        return True

def username_validator(username):
    #Creating a record of all existing usernames to avoid conflict.
    client = pymongo.MongoClient("mongodb+srv://userdata_checker:freehit_userdatachecker@testacoda-001-cj5sj.mongodb.net/test?retryWrites=true&w=majority")
    db = client.freehit_db
    collection = db.user_profile_data
    cursor = collection.distinct("username")
    for existing_username in cursor:
        if username == existing_username:
            return("ErrorCode : ec02")
        else:
            pass
    return True

def email_validator(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex,email)):
        client = pymongo.MongoClient("mongodb+srv://userdata_checker:freehit_userdatachecker@testacoda-001-cj5sj.mongodb.net/test?retryWrites=true&w=majority")
        db = client.freehit_db
        collection = db.user_profile_data
        cursor = collection.distinct("email")
        for existing_email in cursor:
            if existing_email == email:
                return("ErrorCode : ec03")
        return True
    else:
        return("ErrorCode : ec03")

def data_train(opcode,data_string,server_object):
    #data_train is used to send data to the server in form of a
    #concatenated string with a prefix operation code.
    #list of operation codes will determine the type of operation
    #the server performs on/with the data string.
    #list of operation codes will be made public in the repository folder.
    #correct use of the operation code is important for correct operation.

    #passing the object of the server is crucial.

    data_string = opcode + ":" + data_string
    try:
        server_object.send(data_string.encode('ascii'))
        print("Data sent successfully!")
    except:
        print("ErrorCode : ec05")


main(port_checker())
