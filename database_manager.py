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

def addAcc(u_name,u_pw,u_email,query):  
        conn= connectDatabase()       
        if(conn != None):
            cur = conn.cursor()            
            cur.execute(query)
            cur.commit()      
     
def storePass(u_mail,app_email,app_pw,app_name,app_url):
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
                        values('"""+ app_email +"""','"""+ app_pw +"""','"""+app_name+"""','"""+app_url+"""','"""+acc_id+"""')
                        """)
            cur.commit()      
     
def findData(u_email):
    conn = connectDatabase()
    cur = conn.cursor()
    cur.execute("SELECT * FROM account WHERE App_email = '" + u_email +"'")
    cur.fetchall()
    

    #name = input()
    #cur.execute("SELECT * FROM account WHERE Acc_Name = '"+ name +"' ")
    #user=cur.fetchall()
    #print(user[1])


def deleteData(u_name, u_email):
    conn = connectDatabase()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM account WHERE Acc_name = '" + u_name + "' AND lname = '" + u_email + "' ")




  

#connectDatabase()
#addData()
#deleteData()
#findData()
#createTable()
#cur.close()
#conn.close()