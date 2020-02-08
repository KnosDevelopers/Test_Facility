# creating multi threaded server for backend.

import socket
from _thread import *
import threading
from selenium import webdriver
import pymongo


def connection_handler(connection_object):
    while True:
        cmd_data = connection_object.recv(1024)
        data_chunks = (cmd_data.decode('ascii')).split(":")
        operation_handler(data_chunks)

    connection_object.close()

def main():
    host = "192.168.18.68"
    port = 2030
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    print("Socket binded to port ",port)

    server.listen(3)

    while True:
        connection_object,address = server.accept()
        print("Connected to ",address[0],":",address[1])
        threading._start_new_thread(connection_handler,(connection_object,))
    server.close()

def port_updater():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    browser = webdriver.Chrome(chrome_options=options)
    browser.get('http://127.0.0.1:4040/status')
    full_xpath = str("/html/body/div[2]/div/div/div/div[1]/div[1]/ul/li/div/table/tbody/tr[1]/td")
    port_no = (browser.find_element_by_xpath(full_xpath)).text

    client = pymongo.MongoClient("mongodb+srv://port_updater:freehit_portupdater@testacoda-001-cj5sj.mongodb.net/test?retryWrites=true&w=majority")
    db = client.freehit_db
    collection = db.port
    cursor = collection.find({})
    for document in cursor:
        old_port_no = document['port']

    collection.update_one({"port" : old_port_no},{"$set" : {"port" : port_no[21:]}})

def operation_handler(data_chunks):
    #checks for the operation code and performs the operation accordingly.
    op_code = data_chunks[0]
    data_document = {"name":data_chunks[1],"username":data_chunks[2],"email":data_chunks[3],"password":data_chunks[4]}
    if op_code == "op01":
        client = pymongo.MongoClient("mongodb+srv://userdata_updater:freehit_userdataupdater@testacoda-001-cj5sj.mongodb.net/test?retryWrites=true&w=majority")
        db = client.freehit_db
        collection = db.user_profile_data
        collection.insert_one(data_document)

if __name__ == '__main__':
    port_updater()

    main()
