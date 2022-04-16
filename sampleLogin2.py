from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import ImageTk,Image
from database_manager import connectDatabase
from collections import ChainMap
import itertools



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
def cmd():
    if e1.get()=='admin' and e2.get()=='admin':
        messagebox.showinfo("LOGIN SUCCESSFULLY", "         W E L C O M E        ")
        q= Toplevel()     
        q.geometry('700x700')
        q.title('SMF Password Manager')
        q.resizable(0,0)
        

        imagec=Image.open("bg/23.png")
        imaged= ImageTk.PhotoImage(imagec)

        label5 = Label(q,image=imaged,
                       border=0,
               
                       justify=CENTER)


        label5.place(x=0, y=0)
        q.mainloop()
        
    else:
        messagebox.showwarning("LOGIN FAILED","        PLEASE TRY AGAIN        ")


#Button_with hover effect
def bttn(x,y,text,ecolor,lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor #ffcc66
        myButton1['foreground']= lcolor  #000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(w,text=text,
                   width=19,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=cmd)
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)


bttn(90,250,'L O G I N','white','#075064')


w.mainloop()

