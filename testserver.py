import socket
import time
from threading import Thread
clients_groups={}
clients = {}

grp_name_and_pass={}
online_users=[]

ss = socket.socket()
port_number = 8000
ss.bind(("", port_number))
ss.listen()
print("Server is waiting for client.")

def validate(group_name,group_password):
    if group_name in list(grp_name_and_pass.keys()):
        if grp_name_and_pass[group_name]==group_password:
            print((" "*40)+str(group_name)+(" "*40))
            for i in online_users:
                print(i,end="  ")
            return True
        else:
            wrong_password="Wrong Password"
            conn.sendall((wrong_password.encode()))
            time.sleep(3)
            conn.close()
            return False
    else:
        grp_name_and_pass[group_name]=group_password
        print("Successful creation of group : " +str(group_name)+" : "+str(grp_name_and_pass[group_name] ))
        return True

def clients_task(client_name, conn, addr):
    while True:
        data = conn.recv(1000)
        message = client_name + ":" + data.decode()
        for client in clients:
            if client != client_name:
                clients[client].sendall(message.encode())


while True:
    conn, addr = ss.accept()
    print("Server is connected to client at :", addr)

    group_name=conn.recv(1000)
    group_password=conn.recv(1000)
    print(group_name,group_password)
    usr_name=conn.recv(1000)
    print(usr_name)
    if validate(group_name,group_password):

        online_users.append(usr_name)

        clients[usr_name.decode()] = conn
        t = Thread(target=clients_task, args=(usr_name.decode(), conn, addr))
        t.start()
    else:
        print("Boobs")
