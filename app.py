import easygui

myvar = easygui.enterbox("What, is your favorite color?")
print(myvar)





#from tkinter import *
#from tkinter import ttk

#import database_manager as dbm
#from PasswordHasher import *
#import mainloginpage

#root = Toplevel(w)
#root.title('SMF Password Manager')

#root.geometry("1000x500")



#def query_database(name):
#	# Create a database or connect to one that exists
	

#	# Create a cursor instance	
#	query ="Select AccountID from account Where Acc_name = '"+name+"'"      
#	userID = dbm.fetchSingleData(query)	
#	#query = "SELECT * FROM password WHERE AccountID= '"+str(userID)+"'"	
#	records = dbm.findData(userID[0])
	
#	# Add our data to the screen
#	global count
#	count = 0

#	for record in records:
#		if count % 2 == 0:
#			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
#		else:
#			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
#		# increment counter
#		count += 1
#	#decrypt_password(record[2].encode())
		
	



## Add Some Style
#style = ttk.Style()

## Pick A Theme
#style.theme_use('default')

## Configure the Treeview Colors
#style.configure("Treeview",
#	background="#D3D3D3",
#	foreground="black",
#	rowheight=25,
#	fieldbackground="#D3D3D3")

## Change Selected Color
#style.map('Treeview',
#	background=[('selected', "#347083")])

## Create a Treeview Frame
#tree_frame = Frame(root)
#tree_frame.pack(pady=10)

## Create a Treeview Scrollbar
#tree_scroll = Scrollbar(tree_frame)
#tree_scroll.pack(side=RIGHT, fill=Y)

## Create The Treeview
#my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
#my_tree.pack()

## Configure the Scrollbar
#tree_scroll.config(command=my_tree.yview)

## Define Our Columns
#my_tree['columns'] = ("ID", "Acc_name", "Acc_pw", "Acc_salt")

## Format Our Columns
#my_tree.column("#0", width=0, stretch=NO)
#my_tree.column("ID", anchor=W, width=50)
#my_tree.column("Acc_name", anchor=W, width=220)
#my_tree.column("Acc_pw", anchor=CENTER, width=300)
#my_tree.column("Acc_salt", anchor=CENTER, width=300)


## Create Headings
#my_tree.heading("#0", text="", anchor=W)
#my_tree.heading("ID", text="ID", anchor=W)
#my_tree.heading("Acc_name", text="Acc_name", anchor=W)
#my_tree.heading("Acc_pw", text="Acc_pw", anchor=CENTER)
#my_tree.heading("Acc_salt", text="Acc_salt", anchor=CENTER)


## Create Striped Row Tags
#my_tree.tag_configure('oddrow', background="white")
#my_tree.tag_configure('evenrow', background="lightblue")



## Add Record Entry Boxes
#data_frame = LabelFrame(root, text="Record")
#data_frame.pack(fill="x", expand="yes", padx=20)


#ln_label = Label(data_frame, text="Acc_name")
#ln_label.grid(row=0, column=1, padx=10, pady=10)
#ln_entry = Entry(data_frame)
#ln_entry.grid(row=0, column=2, padx=10, pady=10)

#id_label = Label(data_frame, text="Acc_pw")
#id_label.grid(row=0, column=3, padx=10, pady=10)
#id_entry = Entry(data_frame)
#id_entry.grid(row=0, column=4, padx=10, pady=10)

## Move Row Up
#def up():
#	rows = my_tree.selection()
#	for row in rows:
#		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

## Move Rown Down
#def down():
#	rows = my_tree.selection()
#	for row in reversed(rows):
#		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

### Remove one record
##def remove_one():
##	x = my_tree.selection()[0]
##	my_tree.delete(x)

### Remove Many records
##def remove_many():
##	x = my_tree.selection()
##	for record in x:
##		my_tree.delete(record)

### Remove all records
##def remove_all():
##	for record in my_tree.get_children():
##		my_tree.delete(record)

### Clear entry boxes
##def clear_entries():
##	# Clear entry boxes
##	fn_entry.delete(0, END)
##	ln_entry.delete(0, END)
##	id_entry.delete(0, END)
##	address_entry.delete(0, END)
##	city_entry.delete(0, END)
##	state_entry.delete(0, END)
##	zipcode_entry.delete(0, END)


### Select Record
##def select_record(e):
##	# Clear entry boxes
##	fn_entry.delete(0, END)
##	ln_entry.delete(0, END)
##	id_entry.delete(0, END)
##	address_entry.delete(0, END)
##	city_entry.delete(0, END)
##	state_entry.delete(0, END)
##	zipcode_entry.delete(0, END)

##	# Grab record Number
##	selected = my_tree.focus()
##	# Grab record values
##	values = my_tree.item(selected, 'values')

##	# outpus to entry boxes
##	fn_entry.insert(0, values[0])
##	ln_entry.insert(0, values[1])
##	id_entry.insert(0, values[2])
##	address_entry.insert(0, values[3])
##	city_entry.insert(0, values[4])
##	state_entry.insert(0, values[5])
##	zipcode_entry.insert(0, values[6])

### Update record
##def update_record():
##	# Grab the record number
##	selected = my_tree.focus()
##	# Update record
##	my_tree.item(selected, text="", values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(), zipcode_entry.get(),))

##	# Clear entry boxes
##	fn_entry.delete(0, END)
##	ln_entry.delete(0, END)
##	id_entry.delete(0, END)
##	address_entry.delete(0, END)
##	city_entry.delete(0, END)
##	state_entry.delete(0, END)
##	zipcode_entry.delete(0, END)



### Add Buttons
##button_frame = LabelFrame(root, text="Commands")
##button_frame.pack(fill="x", expand="yes", padx=20)

##update_button = Button(button_frame, text="Update Record", command=update_record)
##update_button.grid(row=0, column=0, padx=10, pady=10)

##add_button = Button(button_frame, text="Add Record")
##add_button.grid(row=0, column=1, padx=10, pady=10)

##remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
##remove_all_button.grid(row=0, column=2, padx=10, pady=10)

##remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
##remove_one_button.grid(row=0, column=3, padx=10, pady=10)

##remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
##remove_many_button.grid(row=0, column=4, padx=10, pady=10)

##move_up_button = Button(button_frame, text="Move Up", command=up)
##move_up_button.grid(row=0, column=5, padx=10, pady=10)

##move_down_button = Button(button_frame, text="Move Down", command=down)
##move_down_button.grid(row=0, column=6, padx=10, pady=10)

##select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
##select_record_button.grid(row=0, column=7, padx=10, pady=10)

### Bind the treeview
##my_tree.bind("<ButtonRelease-1>", select_record)

# #Run to pull data from database on start

#userID = 'Pete'
#query_database(userID)

#root.mainloop()

