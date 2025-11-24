pwd = input("Please enter your password: ")

def view():
    pass

def add():


while True:
    mode = input("Would you like to add a new password, or view existing ones? (add, view), press q to quit: ").lower()
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