import database_manager as dbm
from masterHash import * 
from PasswordHasher import *
from tkinter import *
from PIL import ImageTk,Image
import ui_related as ui




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
        ui.popWindow(status,msg)



def userLogin(name,mpw):
   
    
    query = " Select Acc_name, Acc_pw, Acc_salt From account Where Acc_name = '"+name+"' "    
    data = dbm.fetchSingleData(query)
    if(data == None):
        status="LOGIN FAILED"
        msg = "         You don\'t have an account      "
        ui.popWindow(status,msg)        
    else:
        password = addHash(mpw,data[2])
        if password == data[1]:
            closeWin(w)
            sf = Tk()
            sf.iconbitmap('bg/key.ico')
            sf.title(' PLEASE SELECT YOUR KEY ')
            sf.geometry("400x30")
            status="LOGIN SUCCESSFUL" 
            msg = "         WELCOME        " + data[0]
            ui.popWindow(status,msg)
            
            
            #Create a button to save file 
            def open_file():
                key_file = ui.fd.askopenfilename()                
                ui.query_database(name,key_file,sf)                
            btn= Button(sf, text= "FIND KEY", command= lambda:open_file())
            btn.place(x=150,y=7)
            
            sf.mainloop()            
        else:
            status="LOGIN FAILED" 
            msg = "                 "
            ui.popWindow(status,msg)

def closeWin(window):
    window.destroy()



def login():
    name = e1.get()
    mpw = e2.get()
    userLogin(name,mpw)
  
    
    
def register(): 
    name = e1.get()
    mpw = e2.get()
    sf = Tk()
    sf.iconbitmap('bg/key.ico')
    sf.title(' PLEASE SAVE YOUR KEY ')
    sf.geometry("400x30")
    def save_file():
        key_file = ui.fd.asksaveasfile(initialfile = name + '.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        create_key(key_file.name,sf)
        
    #Create a button to save file    
    btn= Button(sf, text= "Select your directory", command= lambda:save_file())
    btn.place(x=150,y=7)

    addUser(name,mpw)
    
    sf.mainloop()

w=Tk()
w.geometry('320x320')
w.iconbitmap('bg/13.ico')
w.title(' L O G I N ')
w.resizable(0,0)
imagea=Image.open("bg/11.png")
imageb= ImageTk.PhotoImage(imagea)
label1 = Label(image=imageb,border=0,justify=CENTER)
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
   
#Button_with hover effect
def bttn(x,y,ecolor,lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor #ffcc66
        myButton1['foreground']= lcolor  #000d33
    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(w,text='L O G I N',width=19,height=2,fg=ecolor,border=0,bg=lcolor,activeforeground=lcolor,activebackground=ecolor,command=login)
    myButton2 = Button(w,text='Register',width=19,height=2,fg=ecolor,border=0,bg=lcolor,activeforeground=lcolor,activebackground=ecolor,command=register)
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)
    

    myButton1.place(x=x,y=y)
    myButton2.place(x=90,y=290)

bttn(90,250,'white','#075064')





w.mainloop()