#import database
import database_manager as dbm
#import fetch file???

# name = input("Enter Username: ")
# password = input("Enter Password: ")




def addUser(name, mpw, mail):
    
    dbm.addAcc(name,mpw,mail)
    






name = "Shakti"
m_password = "Sikka"
email = "shakti.sikka@gmail.com"

addUser(name, m_password, email)