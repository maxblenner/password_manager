#import database as db
#import fetch file
import itertools
from screen import userAccount
from database_manager import addAcc, connectDatabase
from collections import ChainMap

#database connection (use cur to manipulate)
conn= connectDatabase()
cur = conn.cursor()
cur.execute("SELECT * FROM account")
desc= cur.description
column_names = [col[0] for col in desc]
db= dict(ChainMap
         (*
          [dict(zip(column_names, row))  
           for row in cur.fetchall()] 
          )
         ) 
name = "admin"
password = "admin"
msg = "fail"
#db = {"admin": "admin", "asd": "asd"}




def addUser(name, password):
    if name in db:
        print("The username already exists! \nPlease try again")
        createUser()

    else:
        if isinstance(name, str):
            #STORE VALUES TO DATABASE
            #query="INSERT INTO account (Acc_name,Acc_pw,Acc_email) values('"+ name +"','"+ password +"','"+ u_email +"')"
            #addAcc(name,pw,u_email)
            db[name] = password
            print(db)

def createUser():
     name = input("Enter a username: ")
     password = input("Enter a password: ")
     addUser(name, password)

def userScreen(msg, user):
    if msg == "Success":
        sample = userAccount(name=user)
        username, data = sample.userData()
        print(f"Welcome {username}")
        data = data.split(";")
        if data:
            # print(data)
            for i in data:
                i = i.split(":")
                for a in i:
                    print(a, end="  ")
                print()
        else:
            print("No data")

# print(db)


if isinstance(name, str):
    if name in db:
        print("ok")
        if db[name] == password:
            msg = "Success"
            print("Login Successful...")
            userScreen(msg, name)
        else:
            print("Incorrect Password")

    else:
        print("User Does not Exist! Please create new user below: ")
        createUser()
else:
    print("That doesn't look like a Username! Please restart...")
