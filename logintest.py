#import database
import database_manager as dbm
from screentest import userAccount
#import fetch file???

# name = input("Enter Username: ")
# password = input("Enter Password: ")


db = dbm.pullData()

def addUser():
    print("You are not registered..!")
    print("If you want to register ")
    name = input("Please enter a username : ")
    mpw = input("Please enter your password : ")
    u_email = input("Please enter a email : ")
    query="""
            IF NOT EXISTS (SELECT * FROM account 
            WHERE Acc_name= '""" + name + """' OR Acc_email= '""" + u_email +"""') 
            INSERT INTO account (Acc_name,Acc_pw,Acc_email) values('"""+ name +"""','"""+ mpw +"""','"""+ u_email +"""') 
          """
    dbm.addAcc(query)
    
def deleteRecord(userID,mpw,app_email,app_name): 
    pw = input("Please enter your master password: ")
    if(pw == mpw):
        app_name = input("Please enter the name of the app to delete from records..")
        app_email= input("Please enter the email to delete from records..")
        dbm.deleteData(userID,app_email,app_name)




name = "test"
m_password = "test"
email = "test@gmail.com"



def userScreen(msg, userID):
    if msg == "Success":
        sample = userAccount(userID)
        data= sample.fetchData()
        print(f"Welcome {userID}")
        if data:
           for dic in data:
                for key in dic:
                    print("data ==> %s " %key)
                    
        else:
            print("No data")


if isinstance(name, str):
    for dic in db:
        for key in dic:
            if dic[key] == name:
                print("ok")               
                if  m_password == dic['Acc_pw'].strip():
                    msg = "Success"
                    print("Login Successful...")
                    userScreen(msg, dic['AccountID'])
                    break;
                else:
                    print("Incorrect Password")

            #else:
                #print("User Does not Exist! Please create new user below: ")
                #addUser()
else:
    print("That doesn't look like a Username! Please restart...")
