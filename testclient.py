import sys
import socket
from threading import Thread

cs = socket.socket()
port_number = 8000
cs.connect(("localhost", port_number))

group_name=input("Enter Group name : ")
cs.sendall(group_name.encode())

group_password=input("Enter Password : ")
cs.sendall(group_password.encode())

usr_name = input("Username :")
cs.sendall(usr_name.encode())


def receive_data():
    while True:
        data = cs.recv(1000)
        print(data.decode())

def send_data():
    while True:
        usr_data = input()
        cs.sendall(usr_data.encode())

t=Thread(target=receive_data)
t.start()
send_data()
