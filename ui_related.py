from tkinter import *
from tkinter import messagebox
import PasswordHasher as ph
import database_manager as dbm
from tkinter import ttk
from tkinter import filedialog as fd



def popWindow(status,msg):   
   messagebox.showinfo(status, msg)

def query_database(name,key_file,sf):  
    sf.destroy()
    # Create a cursor instance	
    query ="Select AccountID from account Where Acc_name = '"+name+"'"      
    userID = dbm.fetchSingleData(query)	
    records = dbm.findData(userID[0])
    table(records,key_file,userID[0])
	

def table(records,key_file,userID):
    tb = Tk()
    tb.title('SMF Password Manager')
    tb.iconbitmap('bg/13.ico')    
    tb.geometry("900x500")
    
    

    # Add Some Style
    style = ttk.Style()

    # Pick A Theme
    style.theme_use('default')

    # Configure the Treeview Colors
    style.configure("Treeview",
    background="#CCE6E5",
    foreground="black",
    rowheight=25,
    fieldbackground="#CCE6E5")

    # Change Selected Color
    style.map('Treeview',
    background=[('selected', "#347083")])

    # Create a Treeview Frame
    tree_frame = Frame(tb)
    tree_frame.pack(pady=10)

    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create The Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Define Our Columns
    my_tree['columns'] = ("No", "Username", "Password", "Application Name","Application URL")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("No", anchor=W, width=50)
    my_tree.column("Username", anchor=CENTER, width=200)
    my_tree.column("Password", anchor=CENTER, width=200)
    my_tree.column("Application Name", anchor=CENTER, width=200)
    my_tree.column("Application URL", anchor=CENTER, width=200)


    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("No", text="#", anchor=W)
    my_tree.heading("Username", text="Username", anchor=CENTER)
    my_tree.heading("Password", text="Password", anchor=CENTER)
    my_tree.heading("Application Name", text="Application Name", anchor=CENTER)
    my_tree.heading("Application URL", text="Application URL", anchor=CENTER)

    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")
    
    

    global count
    count = 0
    for record in records:
	    if count % 2 == 0:
		    my_tree.insert(parent='', index='end', iid=count, text='', values=(count,record[1],ph.decrypt_password(record[2].encode(),key_file), record[3],record[4]), tags=('evenrow',))
	    else:
		    my_tree.insert(parent='', index='end', iid=count, text='', values=(count,record[1],ph.decrypt_password(record[2].encode(),key_file), record[3],record[4]), tags=('oddrow',))
	    
	    count += 1
    
    # Add Record Entry Boxes
    data_frame = LabelFrame(tb, text="Record")
    data_frame.pack(fill="x", expand="yes", padx=20)


    un_label = Label(data_frame, text="Username")
    un_label.grid(row=0, column=1, padx=10, pady=10)
    un_entry = Entry(data_frame)
    un_entry.grid(row=0, column=2, padx=10, pady=10)

    pw_label = Label(data_frame, text="Password")
    pw_label.grid(row=0, column=3, padx=10, pady=10)
    pw_entry = Entry(data_frame)
    pw_entry.grid(row=0, column=4, padx=10, pady=10)

    an_label = Label(data_frame, text="Application Name")
    an_label.grid(row=0, column=5, padx=10, pady=10)
    an_entry = Entry(data_frame)
    an_entry.grid(row=0, column=6, padx=10, pady=10)

    url_label = Label(data_frame, text="URL")
    url_label.grid(row=0, column=7, padx=10, pady=10)
    url_entry = Entry(data_frame)
    url_entry.grid(row=0, column=8, padx=10, pady=10)

    # Remove record
    def remove_data(username):
        passID = dbm.fetchPassID(userID,username)
        if(passID != None):
            dbm.deleteData(passID)
            r = my_tree.selection()
            for data in r:
                my_tree.delete(data)
        else:
            status = ' No Record '
            msg = 'No record to delete'
            popWindow(status,msg)

        un_entry.delete(0, END)
        pw_entry.delete(0, END)
        an_entry.delete(0, END)
        url_entry.delete(0, END)   	

    # Select Record
    def select_record(e):

        # Clear entry boxes
        un_entry.delete(0, END)
        pw_entry.delete(0, END)
        an_entry.delete(0, END)
        url_entry.delete(0, END)   	

        # Grab record Number
        selected = my_tree.focus()
        # Grab record values
        values = my_tree.item(selected, 'values')
        
       
        # fill the entry boxes if a record is selected
        if (len(selected)):
            un_entry.insert(0, values[1])
            pw_entry.insert(0, values[2])
            an_entry.insert(0, values[3])
            url_entry.insert(0, values[4])
        


    def add_data():        
        
        app_email = un_entry.get()    
        app_pw = pw_entry.get()
        en_pw = ph.encrypt_password(app_pw.encode().decode('ascii'),key_file)
        app_name= an_entry.get()
        app_url= url_entry.get() 
        dbm.storeData(userID,app_email,en_pw,app_name,app_url)
        #Update on ui
        my_tree.insert(parent='', index='end', iid=0, text='', values=(count,app_email,app_pw,app_name,app_url))
        
    
    	
    button_frame = LabelFrame(tb, text="Add&Delete Record")
    button_frame.pack(fill="x", expand="yes", padx=20)

    add_button = Button(button_frame, text="Add Record", command= add_data)
    add_button.grid(row=0, column=1, padx=20, pady=20)

    remove_one_button = Button(button_frame, text="Delete Record", command=lambda:remove_data(un_entry.get()))
    remove_one_button.grid(row=0, column=5, padx=20, pady=20)

    my_tree.bind("<ButtonRelease-1>", select_record)
    tb.mainloop() 

    



