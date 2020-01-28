import socket 
target_ip="127.0.0.1"
target_port=2222
a=4
def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((((ord(char) + a)-65) % 26) + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((((ord(char) + a) - 97) % 26) + 97) 
  
    return result 

#decryption
def decrypt(text,a): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((((ord(char) - a)-65) % 26) + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((((ord(char) - a) - 97) % 26) + 97) 
  
    return result 
#now we are creating UDP socket -- this remains same for sen/rev
#    using ipv4
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#this for senders
#while 5-3:
while True:
    msg=input("please enter your msg:-")
    result=encrypt(msg,a)
    newmsg=result.encode('ascii')  #we are encoding string to byte like object in python3
    s.sendto(newmsg,(target_ip,target_port))  #now we can send to target
    server=s.recvfrom(100)
    newmsg=(server[0].decode('ascii'))
    result=decrypt(newmsg,a)
    print(result)
