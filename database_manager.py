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
def storePass(userID,app_email,app_pw,app_name,app_url):
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

#Fetching user data    
def findData(userID):
    conn = connectDatabase()
    cur = conn.cursor()
    cur.execute("SELECT * FROM password WHERE AccountID = '" + str(userID) +"'")
    return cur.fetchall()

def fetchPassword(app_name,acc_id):
    conn = connectDatabase()
    cur = conn.cursor()
    cur.execute("SELECT * FROM password WHERE App_name = '" + app_name +"' AND AccountID = '"+ str(acc_id) +"'")
    return cur.fetchall()

    #name = input()
    #cur.execute("SELECT * FROM account WHERE Acc_Name = '"+ name +"' ")
    #user=cur.fetchall()
    #print(user[1])


def deleteData(userID, app_email,app_name):
    conn = connectDatabase()
    cur = conn.cursor()    
    cur.execute("DELETE FROM password WHERE AccountID = '" + str(userID) + "' AND  App_name = '" + app_name + "' AND App_email = '" + app_email + "' ")
    cur.commit()


#print(findData(str(2)))
#name = "rrr"
#pw = "furkan" 
#u_email = "furkan@gmail.com"
#query="INSERT INTO account (Acc_name,Acc_pw,Acc_email) values('"+ name +"','"+ pw +"','"+ u_email +"')"
#addAcc(name,pw,u_email,query)
#storePass(2,'asd@gmail.com','12345','asd','asd.com')
#deleteData(3,'facebook','face')

#print(findData(1))