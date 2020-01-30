class a:
    def new_data(self):
        group_name=input()
        group_password=input()
        usr_name=input()
        new_group_and_password=group_name+":"+group_password+"\n"
        q.groups_and_passwords_write('groups_and_passwords.txt',new_group_and_password)
        q.group_users_write(group_name,(usr_name+"\n"))

    def group_users_write(self,group_name,write_into_file):
        try:
            file=open(("groups/"+str(group_name)+".txt"),"w")
            file.write(write_into_file)
        except Exception as e:
            print(e)
    def group_users_read(self,group_name):
        try:
            file=open("groups/"+group_name,"r")
            lines=file.readlines()
            for line in lines:
                print(line)
        except  Exception as e:
            print("group_users_read : "+e)

    def groups_and_passwords_write(self,open_file,write_into_file):
        try:
            file=open(open_file,'a')
            file.write(write_into_file)
        except:
            print("groups_and_passwords_write : Error")

    def groups_and_passwords_read(self):
        try:
            file=open('groups_and_passwords.txt','r')
            lines=file.readlines()
            total_data=[]
            for line in lines:
                total_data=line.split(':')
                for data in total_data:
                    print(data)
        except:
            print("groups_and_passwords_read : error")

if __name__=='__main__':
    q=a()
#    q.new_data()
    print("-"*99)
    q.groups_and_passwords_read()
    print("-"*99)
    q.group_users_read("mygroup.txt")
