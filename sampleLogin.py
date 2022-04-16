from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

tkWindow = Tk()
tkWindow.title('Login For SMF')
tkWindow.geometry('320x320')

bg = PhotoImage(file="bg/11.png")

my_canvas = Canvas(tkWindow, width=320, height=320 )
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg, anchor="nw")

my_canvas.create_text(200,200,text="Password Manager")


usernameLabel = Label(tkWindow, text="User Name")
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username)

passwordLabel = Label(tkWindow,text="Password")
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*')

validateLogin = partial(validateLogin, username, password)

loginButton = Button(tkWindow, text="Login", command=validateLogin)

tkWindow.mainloop()