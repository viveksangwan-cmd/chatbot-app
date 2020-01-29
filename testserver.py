import socket
import time
from threading import Thread
clients_groups={}
clients = {}

grp_name_and_pass={}
online_users=[]

grp_name_and_users={}


ss = socket.socket()
port_number = 8000
ss.bind(("", port_number))
ss.listen()
print("Server is waiting for client.")

def validate(group_name,group_password):
    if group_name in list(grp_name_and_pass.keys()):
        if grp_name_and_pass[group_name]==group_password:
            for i in online_users:
                user=str(i)
                conn.sendall(user.encode())
            grp_name_and_users[group_name].append(usr_name)
            print(grp_name_and_users,grp_name_and_users[group_name])
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
        grp_name_and_users[group_name]=[]
        grp_name_and_users[group_name].append(usr_name)
        print(grp_name_and_users,grp_name_and_users[group_name])
        return True

def clients_task(usr_name, conn, addr):
    while True:
        data = conn.recv(1000)
        message = usr_name + ":" + data.decode()
        for users in grp_name_and_users[group_name]:
            if users in online_users:
                for client in clients:
                    if client!=usr_name:
                        print(users,usr_name)
                        clients[users].sendall(message.encode())
            else:
                print("user is not online")
                break

while True:
    conn, addr = ss.accept()
    print("Server is connected to client at :", addr)

    group_name=conn.recv(1000).decode()
    group_password=conn.recv(1000).decode()
    print(group_name,group_password)
    usr_name=conn.recv(1000).decode()
    print(usr_name)
    if validate(group_name,group_password):

        online_users.append(usr_name)
        print("online_users :",online_users)
        clients[usr_name] = conn

        print(clients)

        t = Thread(target=clients_task, args=(usr_name, conn, addr))
        t.start()
    else:
        print("--------------")
