import socket
from threading import Thread
clients_groups={}
clients = {}
grp_name_and_pass={}
ss = socket.socket()
port_number = 8000
ss.bind(("", port_number))
ss.listen()
print("Server is waiting for client.")


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
    print(group_name.decode())

    group_password=conn.recv(1000)
    print(group_password.decode())

    print(grp_name_and_pass.keys())

    if group_name in list(grp_name_and_pass.keys()):
        if grp_name_and_pass[group_name]==group_password:
            print("success")

            usr_name = conn.recv(1000)
            clients[usr_name.decode()] = conn
            t = Thread(target=clients_task, args=(usr_name.decode(), conn, addr))
            t.start()

        else:
            print("wrong password")
    else:
        print("new group")
        grp_name_and_pass[group_name]=group_password
