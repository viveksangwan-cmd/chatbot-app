import socket,select
from crypto.cipher import AES

def encrypt(raw):
    cipher = AES.new('key123',AES.MODE_CFB,'this is an IV456')
    return(ciper.encypt(raw))
def decrypt(enc):
    cipher = AES.new('key123',AES.MODE_CFB,'this is an IV456')
    return(ciper.decrypt(enc))
def prompt():
    sys.stdout.write('<you> \n')
    sys.stdout.flush()

if __name__ == "__main__":

    if(len(sys.argv)<3):
        print("usage : python client_one.py hostname port")
        sys.exit()

    host = sys.argv[1]
    port = sys.argv[2]

    s = socket.socket(socket.AF_INET,scoket.SOCK_STREAM)
    s.settimeout(2)

    try :
        s.connect((host,port))
    except:
        print("connection failed")
    print("Connection established, send your first message")
    prompt()

    while 1:
        socket_list = [sys.stdin,s]

        read_sockets,write_sockets,error_sockets = select.select(socket_list,[],[])

        for sock in read_sockets:

         if sock == s:
            data = sock.recv(200)
            if not data:
                print("Disconnected")
                sys.exit()
            else:
                data1 = str(data[24:])
                decoded_chat=decrypt(data1)
                sys.stdout.write(decoded_chat)
                prompt()
         else:
            msg = sys.stdin.readline()
            encrypted_chat=encrypt(msg)
            s.send(encrypted_chat)
            prompt()

            
                





                











        
