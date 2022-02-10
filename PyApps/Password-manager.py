from cryptography.fernet import Fernet 

print("HELLO, AND WELCOME TO THIS PASSWORD MANAGER APP")
print("THIS APP IS NOT ENCRYPTED, DONT INSERT BANK OR IMPORTANT PASSWORDS")
print("-----------------------------------------------------------------------")
master_pwd = input("What is the master password?: ")


def write_key():

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()        

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

'''key = load_key() + master_pwd
fer = Fernet(key)'''



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw.encode())

def add():
    name = input("Account Name: ")
    pwd = input("Passowrd: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones? Type Q to quit. (view,add): ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue