import database_manager as dbm
from masterHash import * 
import time
import pandas as pd
from PasswordHasher import *




conn= dbm.connectDatabase()
cur = conn.cursor()

db = dbm.fetchAccounts()








#a = [
#    {'main_color': 'red', 'second_color':'blue'},
#    {'main_color': 'yellow', 'second_color':'green'},
#    {'main_color': 'yellow', 'second_color':'blue'},
#]

#string = 'AccoundID'
#color = '1'
#if  any(d[string] == color for d in db):
#    print(a[0].keys())

##print(type(db))
##print(db[0].keys())

def addUser(name,mpw):

    salt= genSalt().decode('ascii')
    mpw = mpw + salt
    mpw = hashInput(mpw.encode()).decode('ascii') 
    create_key()

    query="INSERT INTO account (Acc_name,Acc_pw,Acc_salt) values('"+ name +"','"+ mpw +"','"+ salt +"')"
    dbm.addAcc(query)




def userLogin(name,mpw): 
    query = " Select Acc_name, Acc_pw, Acc_salt From account Where Acc_name = '"+name+"' "    
    data = dbm.fetchSingleData(query)
    if(data == None):
        print("User does not exists")
        name = input("Put your name ")
        mpw = input("Put your password ")
        addUser(name,mpw)
    else:
        password = addHash(mpw,data[2])
        if password == data[1]:
            print("Welcome",data[0])
            print("fetching Data...")
            time.sleep(1)
            userData(name)
        
        
def userData(name):
    query="Select AccountID from account Where Acc_name = '"+name+"'"      
    userID=dbm.fetchSingleData(query)
    userData=dbm.findData(userID[0])

    
    
    if userData == []:
        print("No records found... ")
        storeData(userID[0])

    else:
        app_name = input("Please enter a name : ")
        passwords = dbm.fetchPassword(app_name,userID[0])
        print(decrypt_password(passwords[0][2].encode()))
        storeData(userID[0])
    
       

def storeData(userID):
    app_email=input("Please put the username address for the app: ")    
    app_pw=input("Please put the password for the app: ")
    app_pw = encrypt_password(app_pw.encode()).decode('ascii')
    app_name=input("Please put the name for the app: ")
    app_url=input("Please put the url for the app: ")  
    dbm.storePass(userID,app_email,app_pw,app_name,app_url)



       
name = input("Please put your name: ")
mpw = input("Please put your mpw: ")
userLogin(name,mpw)