master_pwd = input("Please enter the master password: ")

def view():
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            # split string between account name and password
            user, passw = data.split("|")
            print(f"Account Name: {user} | Password: {passw}")

def add():
    name = input("\nAccount Name: ")
    pwd = input("Password: ")

    # auto closes file
    with open("passwords.txt", "a") as file:
        file.write(f"{name} | {pwd}\n")



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