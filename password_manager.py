# encryption module
from cryptography.fernet import Fernet

# only needs calling once to create key
'''
def write_key():
    key = Fernet.generate_key()
    # write bytes mode 'wb'
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    # read bytes mode 'rb'
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
# initialising encryption module
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            # split string between account name and password
            user, passw = data.split("|")
            print(f"Account Name: {user} | Password: {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input("\nAccount Name: ")
    pwd = input("Password: ")

    # auto closes file
    with open("passwords.txt", "a") as file:
        # encode pwd to turn to byte str, then decode to regular str
        file.write(f"{name} | {fer.encrypt(pwd.encode()).decode()}\n")

while True:
    mode = input("\nWould you like to add a new password, or view existing ones? (add, view), press q to quit: ").lower()
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Please enter either 'add' or 'view'.")
        # re-enter while True loop
        continue