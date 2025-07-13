from cryptography.fernet import Fernet

# Uncomment the line below to generate a new key
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter your master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, enc_pwd = data.split("|")
            print(f"Account: {name} | Password: {fer.decrypt(enc_pwd.encode()).decode()}")

def add():
    name = input("Enter the name of the account: ")
    pwd = input("Enter the password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing passwords or quit? (add/view/q): ").lower()
    if mode == "q":
        break

    elif mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("Invalid option. Please choose 'add' or 'view'.")
        continue

