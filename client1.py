#!/usr/bin/python3
#client.py

import socket

host = '192.168.187.68'
port = 2001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("You are connected to server")

def send_and_receive():
    data = s.recv(1024)
    print(data.decode())

    s.send(data)

for i in range(11):
    try:
        send_and_receive()
    except ConnectionRefusedError:
        print("The server is not accepting our connection request!")
        #exit(1)
   
    print ("This sentence will only print if the except block was not executed.")
