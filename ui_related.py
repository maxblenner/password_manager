from tkinter import *
from tkinter import messagebox
import PasswordHasher as ph
import database_manager as dbm
import easygui
#from mainloginpage import userLogin,addUser

def sendFileName(fn):
    ph.create_key(fn)
def valid_input(text):
    not_valid = True
    res = ''
    while not_valid:
        res = easygui.enterbox("Please enter the file name which has your private key")
        if res.split():  # if text is empty or only spaces, this creates an empty list evaluated at False
            not_valid = False
    return res            
    
def popWindow(status,msg):   
   messagebox.showinfo(status, msg)

def query_database(name,key_file):
    # Create a database or connect to one that exists
   
    # Create a cursor instance	
    query ="Select AccountID from account Where Acc_name = '"+name+"'"      
    userID = dbm.fetchSingleData(query)	
    #query = "SELECT * FROM password WHERE AccountID= '"+str(userID)+"'"	
    records = dbm.findData(userID[0])
    table(records,key_file)
	#passwords = dbm.fetchPassword(app_name,userID[0])
 #   pw= decrypt_password(passwords[0][2].encode())       
 #   print(passwords[0][1], end = " ")

def table(records,key_file):
    tb = Tk()
    tb.title('SMF Password Manager')
    tb.iconbitmap('bg/13.ico')
    tb.geometry("1000x500")


    # Add Some Style
    style = ttk.Style()

    # Pick A Theme
    style.theme_use('default')

    # Configure the Treeview Colors
    style.configure("Treeview",
	    background="#D3D3D3",
	    foreground="black",
	    rowheight=25,
	    fieldbackground="#D3D3D3")

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
    my_tree['columns'] = ("ID", "Acc_name", "Acc_pw", "Acc_salt")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID", anchor=W, width=50)
    my_tree.column("Acc_name", anchor=W, width=220)
    my_tree.column("Acc_pw", anchor=CENTER, width=300)
    my_tree.column("Acc_salt", anchor=CENTER, width=300)


    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID", text="ID", anchor=W)
    my_tree.heading("Acc_name", text="Acc_name", anchor=W)
    my_tree.heading("Acc_pw", text="Acc_pw", anchor=CENTER)
    my_tree.heading("Acc_salt", text="Acc_salt", anchor=CENTER)


    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")
    
   
    global count
    count = 0
    for record in records:
	    if count % 2 == 0:
		    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1],decrypt_password(record[2].encode(),key_file), record[3]), tags=('evenrow',))
	    else:
		    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1],decrypt_password(record[2].encode(),key_file), record[3]), tags=('oddrow',))
	    
	    count += 1
    
    ## Add Record Entry Boxes
    #data_frame = LabelFrame(tb, text="Record")
    #data_frame.pack(fill="x", expand="yes", padx=20)


    #ln_label = Label(data_frame, text="Acc_name")
    #ln_label.grid(row=0, column=1, padx=10, pady=10)
    #ln_entry = Entry(data_frame)
    #ln_entry.grid(row=0, column=2, padx=10, pady=10)

    #id_label = Label(data_frame, text="Acc_pw")
    #id_label.grid(row=0, column=3, padx=10, pady=10)
    #id_entry = Entry(data_frame)
    #id_entry.grid(row=0, column=4, padx=10, pady=10)
    ### Remove one record
    #def remove_one():
    #	x = my_tree.selection()[0]
    #	my_tree.delete(x)

    ## Remove Many records
    #def remove_many():
    #	x = my_tree.selection()
    #	for record in x:
    #		my_tree.delete(record)

    ## Remove all records
    #def remove_all():
    #	for record in my_tree.get_children():
    #		my_tree.delete(record)

    ## Clear entry boxes
    #def clear_entries():
    #	# Clear entry boxes
    #	fn_entry.delete(0, END)
    #	ln_entry.delete(0, END)
    #	id_entry.delete(0, END)
    #	address_entry.delete(0, END)
    #	city_entry.delete(0, END)
    #	state_entry.delete(0, END)
    #	zipcode_entry.delete(0, END)


    ## Select Record
    #def select_record(e):
    #	# Clear entry boxes
    #	fn_entry.delete(0, END)
    #	ln_entry.delete(0, END)
    #	id_entry.delete(0, END)
    #	address_entry.delete(0, END)
    #	city_entry.delete(0, END)
    #	state_entry.delete(0, END)
    #	zipcode_entry.delete(0, END)

    #	# Grab record Number
    #	selected = my_tree.focus()
    #	# Grab record values
    #	values = my_tree.item(selected, 'values')

    #	# outpus to entry boxes
    #	fn_entry.insert(0, values[0])
    #	ln_entry.insert(0, values[1])
    #	id_entry.insert(0, values[2])
    #	address_entry.insert(0, values[3])
    #	city_entry.insert(0, values[4])
    #	state_entry.insert(0, values[5])
    #	zipcode_entry.insert(0, values[6])

    ## Update record
    #def update_record():
    #	# Grab the record number
    #	selected = my_tree.focus()
    #	# Update record
    #	my_tree.item(selected, text="", values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get(),))

    #	# Clear entry boxes
    #	fn_entry.delete(0, END)
    #	ln_entry.delete(0, END)
    #	id_entry.delete(0, END)
    #	address_entry.delete(0, END)
    #	city_entry.delete(0, END)
    #	state_entry.delete(0, END)
    #	zipcode_entry.delete(0, END)
   

    tb.mainloop() 








