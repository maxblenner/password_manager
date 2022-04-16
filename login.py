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
db=[dict(zip(column_names, row))  
    for row in cur.fetchall()] 
        
#print(db)





def addUser(name, password,u_email):
    #print()
    if name == db.get('Acc_name'):
        print("The username already exists! \nPlease try again")
        createUser()

    else:
        if isinstance(name, str):
            #STORE VALUES TO DATABASE
            query="INSERT INTO account (Acc_name,Acc_pw,Acc_email) values('"+ name +"','"+ password +"','"+ u_email +"')"
            addAcc(name,password,u_email,query)
            #db[name] = password



    
            

def createUser():
     name = input("Enter a username: ")
     password = input("Enter a password: ")
     addUser(name, password,u_email)

def userScreen(msg, user):
    if msg == "Success":
        sample = userAccount(id = user)
        username,data = sample.userData()
        
        print(f"Welcome {username}")       
        if data:
            print(data)
        else:
            print("No data")



#name = input("Please enter the Username : ")
#password = input("Please enter the master password : ")
#u_email = input("Please enter user email : ")
name = 'Shakti'
password = 'Sikka'
u_email = 'shakti.sikka@gmail.com'
msg = "fail"

if isinstance(name, str):
    for dic in db:
        for key in dic:
            #print(key)
            if dic[key] == name:
                print("ok")               
                if  password == dic['Acc_pw'].strip():
                    msg = "Success"
                    print("Login Successful...")
                    userScreen(msg, dic['AccountID'])
                    break;
                else:
                    print("Incorrect Password")

            #else:
            #    print("User Does not Exist! Please create new user below: ")
            #    createUser()
else:
    print("That doesn't look like a Username! Please restart...")
