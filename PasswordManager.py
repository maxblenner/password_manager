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

def addData():  
        conn= connectDatabase()
        fname=input()
        lname=input()
        if(conn != None):
            cur = conn.cursor()
            
            cur.execute("""IF NOT EXISTS (SELECT * FROM account WHERE fname= '""" + fname + """' AND lname= '""" + lname +"""') INSERT INTO account values('"""+ fname +"""','"""+lname+"""')""")
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
conn.close()