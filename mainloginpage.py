import database_manager as dbm
from masterHashing import * 
import time
from PasswordHasher import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os
import userData




def addUser(name,mpw):

    salt= genSalt().decode('ascii')
    mpw = mpw + salt
    mpw = hashInput(mpw.encode()).decode('ascii') 
    query = "Select * from account Where Acc_name = '"+name+"'"
    exists = dbm.fetchSingleData(query)
    if exists == None:
        query="INSERT INTO account (Acc_name,Acc_pw,Acc_salt) values('"+ name +"','"+ mpw +"','"+ salt +"')"
        dbm.addAcc(query)
    else : 
        status="REGISTER FAILED" 
        msg = "         USERNAME EXISTS        " 
        popWindow(status,msg)



def userLogin(name,mpw): 
    query = " Select Acc_name, Acc_pw, Acc_salt From account Where Acc_name = '"+name+"' "    
    data = dbm.fetchSingleData(query)
    if(data == None):
        status="LOGIN FAILED"
        msg = "         You don\'t have an account      "
        popWindow(status,msg)        
    else:
        password = addHash(mpw,data[2])
        if password == data[1]:
            status="LOGIN SUCCESSFUL" 
            msg = "         WELCOME        " + data[0]
            popWindow(status,msg)            
            time.sleep(1)           
            userData(name)
        else:
            status="LOGIN FAILED" 
            msg = "         WRONG PASSWORD        "
            popWindow(status,msg)
        
        
def userData(name):
    query="Select AccountID from account Where Acc_name = '"+name+"'"      
    userID=dbm.fetchSingleData(query)
    userData=dbm.findData(userID[0])
    if userData == []:
        print("No records found... ")
        storeData(userID[0])

    else:
        app_name = input("Please enter a app name : ")
        passwords = dbm.fetchPassword(app_name,userID[0])
        pw= decrypt_password(passwords[0][2].encode())       
        print(passwords[0][1], end = " ")
        print(pw)
        storeData(userID[0])
    
       

def storeData(userID):
    app_email=input("Please put the username address for the app: ")    
    app_pw=input("Please put the password for the app: ")
    app_pw = encrypt_password(app_pw.encode()).decode('ascii')
    app_name=input("Please put the name for the app: ")
    app_url=input("Please put the url for the app: ")  
    dbm.storePass(userID,app_email,app_pw,app_name,app_url)    
    exit()



w=Tk()
w.geometry('320x320')
w.title(' L O G I N ')
w.resizable(0,0)

imagea=Image.open("bg/11.png")
imageb= ImageTk.PhotoImage(imagea)





label1 = Label(image=imageb,
               border=0,
               
               justify=CENTER)


label1.place(x=0, y=0)


l1=Label(w,text='Username',bg='white')
l=('Consolas',13)
l1.config(font=l,bg="#0D7B99")
l1.place(x=120,y=90)

#e1 entry for username entry
e1=Entry(w,width=15,border=0)
l=('Consolas',13)
e1.config(font=l,bg="#075064")
e1.place(x=90,y=120)

#e2 entry for password entry
e2=Entry(w,width=15,border=0,show='*')
e2.config(font=l,bg="#075064")
e2.place(x=90,y=175)


l2=Label(w,text='Password',bg='white')
l=('Consolas',13)
l2.config(font=l,bg="#0D7B99")
l2.place(x=120,y=145)




#Command
def login():
    name = e1.get()
    mpw = e2.get()
    userLogin(name,mpw)
    
def register(): 
    name = e1.get()
    mpw = e2.get()
    pop= Toplevel(w)
    pop.geometry("250x250")
    pop.title("")
    Label(pop, text= "Welcome", font=('Arial',10)).place(x=90,y=20)
    Label(pop, text= "Please enter a file name to store your key ", font=('Arial',10)).place(x=0,y=50)
    entry = Entry(pop,width=15,border=0)
    entry.place(x=70,y=90)
    print(entry.get())
    Button(pop,text= "Create", command= lambda:[sendFileName(entry.get()),pop.destroy()]).place(x=90,y=130)
    
    
    addUser(name,mpw)

    
    pop.mainloop()

def sendFileName(fn):
    create_key(fn)
    
    
def popWindow(status,msg):   
   messagebox.showinfo(status, msg)
   







#Button_with hover effect
def bttn(x,y,ecolor,lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor #ffcc66
        myButton1['foreground']= lcolor  #000d33
    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(w,text='L O G I N',
                   width=19,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=login)
    myButton2 = Button(w,text='Register',
                   width=19,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=register)
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)
    

    myButton1.place(x=x,y=y)
    myButton2.place(x=90,y=290)

bttn(90,250,'white','#075064')




w.mainloop()