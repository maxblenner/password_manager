import pyodbc

#connecting to database
def connectDatabase():

    try:
            conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-9GK1BVN\SQLEXPRESS;'
            'DATABASE=PassManager;'
            'Trusted_Connection=yes;'
            )            
            return conn

    except (Exception, pyodbc.Error):
            print('Unable to connect to database')

def addAcc(name,mpw,email):  
        conn= connectDatabase()       
        if(conn != None):
            cur = conn.cursor()            
            cur.execute
            cur.commit()      
     
def storePass(u_mail,app_email,apw,app_name,app_url):
        conn = connectDatabase()
        if(conn != None):
            cur = conn.cursor()
            acc_id = cur.execute("""
                                 (SELECT AccountID from account 
                                 WHERE Acc_email = '""" + u_mail + """')   
                                """)
            cur.execute("""
                        IF NOT EXISTS (SELECT * FROM password 
                        WHERE App_name= '""" + app_name + """' AND App_email= '""" + app_email +"""') 
                        INSERT INTO password (App_email,App_pass,App_name,App_url,AccountID) 
                        values('"""+ app_email +"""','"""+ apw +"""','"""+app_name+"""','"""+app_url+"""','"""+acc_id+"""')
                        """)
            cur.commit()      
     
def findData():
    conn = connectDatabase()
    cur = conn.cursor()
    name = input()
    cur.execute("SELECT * FROM account WHERE fname = '"+ name +"' ")
    user=cur.fetchall()
    print(user)


def deleteData():
    conn = connectDatabase()
    cur = conn.cursor()
    fname = input()
    lname = input()
    cur.execute("DELETE FROM account WHERE fname = '" + fname + "' AND lname = '" + lname + "' ")

def createTable():    

    #data_type= input('Data type:')
    
    conn = connectDatabase()
    cur = conn.cursor()
    #cur.execute( """IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='link' AND xtype='U') CREATE TABLE link (pid tinyint,url varchar(20))""") #IF EXISTS statement to check if the table is already in database.  
    cur.execute("""Create TABLE pass (pid varchar(MAX),url varchar(MAX))""")
    #cur.execute("Create TABLE account (fname nvarchar(50),lname nvarchar(50))")
    conn.commit()
    



#connectDatabase()
#addData()
#deleteData()
#findData()
#createTable()
#cur.close()
#conn.close()