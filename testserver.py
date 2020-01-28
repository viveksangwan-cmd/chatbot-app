import socket
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
            print((" "*40)+group_name+(" "*40))
            for i in online_users:
                print(i,end="  ")
            print((" "*40)+sys.timestrap()+(" "*40))
        else:
            print("Wrong password")


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
    usr_name=conn.recv(1000)
    print(group_name,group_password,usr_name)
    validate(group_name,group_password)

    online_users.append(usr_name)

    usr_name = conn.recv(20)

    clients[usr_name.decode()] = conn
    t = Thread(target=clients_task, args=(usr_name.decode(), conn, addr))
    t.start()
