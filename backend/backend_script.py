# creating multi threaded server for backend.

import socket
from _thread import *
import threading
from selenium import webdriver
import pymongo


def connection_handler(connection_object):
    while True:
        cmd_data = connection_object.recv(1024)
        if not cmd_data:
            print("No command received. Ending connection.")
            break
        print(cmd_data.decode('ascii'))
        
        connection_object.send(cmd_data)
    connection_object.close()

def main():
    host = "192.168.18.89"
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
    browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    browser.get('http://127.0.0.1:4040/status')
    full_xpath = str("/html/body/div[2]/div/div/div/div[1]/div[1]/ul/li/div/table/tbody/tr[1]/td")
    port_no = (browser.find_element_by_xpath(full_xpath)).text

    client = pymongo.MongoClient("mongodb+srv://portupdater:freehitportupdater@testacoda-001-cj5sj.mongodb.net/test?retryWrites=true&w=majority")
    db = client.freehit_db
    collection = db.port
    collection.update_one({"port"},{"$set" : {"port" : port_no}})
if __name__ == '__main__':
    port_updater()
    main()