# creating multi threaded server for backend.

import socket
from _thread import *
import threading

lock = threading.Lock()

def connection_handler(connection_object):
    while True:
        cmd_data = connection_object.recv(1024)
        if not cmd_data:
            print("No command received. Ending connection.")
            lock.release()
            break
        print(cmd_data)
        
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
        lock.acquire()
        print("Connected to ",address[0],":",address[1])
        start_new_thread(connection_handler,(connection_object))
    server.close()

if __name__ == '__main__':
    main()