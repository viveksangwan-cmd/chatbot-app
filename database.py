class a:
    def new_data(self):
        group_name=input()
        group_password=input()
        usr_name=input()
        new_group_and_password=group_name+":"+group_password+"\n"
        q.groups_and_passwords_write('groups_and_passwords.txt',new_group_and_password,group_name)
        q.group_users_write(group_name,(usr_name+"\n"),(usr_name+"\n"))
        q.print_group_users(group_name)

    def check_user(self,group_name,usr_name):
        flag=True
        try:
            file=open(("groups/"+str(group_name)+".txt"),"r")
            lines=file.readlines()
            if len(lines)>0:
                for line in lines:
                    print(line,usr_name)
                    if line==usr_name:
                        print("User already exits.")
                        return False
            return True
        except Exception as e:
            print("check_user : ",e)

    def group_users_write(self,group_name,write_into_file,usr_name):
        if self.check_user(group_name,usr_name):
            try:
                file=open(("groups/"+str(group_name)+".txt"),"a+")
                file.write(write_into_file)
                print("Successfuly added.")
            except Exception as e:
                print(e)
            finally:
                file.close()

    def group_users_read(self,group_name):
        try:
            file=open("groups/"+group_name,"r")
            lines=file.readlines()
            for line in lines:
                print(line)
            file.close()
        except  Exception as e:
            print("group_users_read : "+e)

    def groups_and_passwords_write(self,open_file,write_into_file,group_name):
        try:
            file=open(open_file,'a+')
            lines=file.readlines()
            if len(lines)>0:
                for line in lines:
                    group_name_and_password=line.split(':')
                    print(group_name_and_password[0])
                    if group_name_and_password[0]==group_name:
                        print("Group already exits")
                        break
            else:
                file.write(write_into_file)
            file.close()
        except Exception as e:
            print("groups_and_passwords_write : "+e)

    def groups_and_passwords_read(self,group_name):
        try:
            file=open("groups/"+group_name+".txt","r")
            lines=file.readlines()
            total_data=[]
            for line in lines:
                total_data=line.split(':')
                for data in total_data:
                    print(data)
            file.close()
        except Exception as e:
            print("groups_and_passwords_read : ",e)

    def print_group_users(self,group_name):
        print("-"*99)
        try:
            file=open(("groups/"+str(group_name)+".txt"),"r+")
            lines=file.readlines()
            for line in lines:
                print(line)
            file.close()
        except Exception as e:
            print("groups_users_write : ",e)
        print("-"*99)


    def print_groups_and_passwords(self):
        print("-"*99)
        group_name=input()
        q.groups_and_passwords_read(group_name)
        print("-"*99)


if __name__=='__main__':
    q=a()
    q.new_data()
