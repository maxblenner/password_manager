#import database as db
#import fetch file

# name = input("Enter Username: ")
# password = input("Enter Password: ")

name = "admin"
password = "admin"

db = {"admin": "admin", "asd": "asd"}

def addUser(name, password):
    if name in db:
        print("The username already exists! \nPlease try again")
        createUser()

    else:
        if isinstance(name, str):
            #STORE VALUES TO DATABASE
            db[name] = password
            print(db)

def createUser():
     name = input("Enter a username: ")
     password = input("Enter a password: ")
     addUser(name, password)

# print(db)
if isinstance(name, str):
    if name in db:
        print("ok")
        if db[name] == password:
            print("Login Successful...")
        else:
            print("Incorrect Password")

    else:
        print("User Does not Exist! Please create new user below: ")
        createUser()
else:
    print("That doesn't look like a Username! Please restart...")
