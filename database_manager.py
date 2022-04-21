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

def fetchAccounts():
    conn=connectDatabase()
    cur = conn.cursor()
    cur.execute("SELECT * FROM account ")
    desc= cur.description
    column_names = [col[0] for col in desc]
    db= [dict(zip(column_names, row))  
            for row in cur.fetchall()]
    return db



#fetching unique user from database
def fetchSingleAccount():
    conn=connectDatabase()
    cur = conn.cursor()
    cur.execute("SELECT AccountID FROM account ")
    desc= cur.description
    column_names = [col[0] for col in desc]
    db= [dict(zip(column_names, row))  
            for row in cur.fetchall()]
    return db

#fetching single data with given query
def fetchSingleData(query):
    conn= connectDatabase()
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchone()

#adding accounts to the database
def addAcc(query):  
        conn= connectDatabase()       
        if(conn != None):
            cur = conn.cursor()            
            cur.execute(query)
            cur.commit()      
#store user password according to userID    
def storeData(userID,app_email,app_pw,app_name,app_url):
        conn = connectDatabase()
        if(conn != None):
            cur = conn.cursor()
            cur.execute("""
                        IF NOT EXISTS (SELECT * FROM password 
                        WHERE App_name= '""" + app_name + """' AND App_email= '""" + app_email +"""') 
                        INSERT INTO password (App_email,App_pass,App_name,App_url,AccountID) 
                        values('"""+ app_email +"""','"""+ app_pw +"""','"""+app_name+"""','"""+app_url+"""','"""+str(userID)+"""')
                        """)
            cur.commit()      
def updateData(passID,app_email,app_pw,app_name,app_url):
    conn = connectDatabase()
    if(conn != None):
            cur = conn.cursor()           
            cur.execute("UPDATE password SET App_email = '"+ app_email +"', App_pass = '"+ app_pw +"', App_name = '"+ app_name +"', App_url = '"+ app_url +"' WHERE PassID = '"+str(passID[0])+"'")
                        
            cur.commit()      

def deleteData(passID):
    conn = connectDatabase()
    if(conn != None):
            cur = conn.cursor()           
            cur.execute("DELETE FROM password WHERE PassID = '"+str(passID[0])+"'")
            cur.commit()      

  
def findData(userID):
    conn = connectDatabase()
    cur = conn.cursor()
    cur.execute("SELECT * FROM password WHERE AccountID = '" + str(userID) +"'")
    return cur.fetchall()

def fetchPassID(userID,userName):
    conn = connectDatabase()
    cur = conn.cursor()
    cur.execute("SELECT PassID FROM password WHERE AccountID = '"+ str(userID) +"' AND App_email = '"+ userName +"' ")
    return cur.fetchone()

def fetchuserName(passID,prevName):
    conn = connectDatabase()
    cur = conn.cursor()
    cur.execute("SELECT App_email FROM password WHERE App_email = '"+ prevName +"' AND PassID = '"+ str(passID[0][0]) +"' ")
    return cur.fetchone()
   