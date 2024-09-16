master_pwd = input("What is the master password ?")


def view():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user",user,"password",passw)

def add():
    name = input("Account name")
    pwd = input("Password")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("would you like to add a new pwd or view existing pwd type view or add").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalide mdoe")
        continue

