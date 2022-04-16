#import database file
from database_manager import addAcc, connectDatabase
from collections import ChainMap
# name = input("Enter Username: ")
# password = input("Enter Password: ")



class userAccount(object):
    """docstring for userAccount."""

    def __init__(self, id=None, password=None):
        super(userAccount, self).__init__()
        self._name = id
        self._password = password

    def userData(self):
        #fetch user data
        conn= connectDatabase()
        cur = conn.cursor()
        cur.execute("SELECT * FROM account")
        desc= cur.description
        column_names = [col[0] for col in desc]
        db= [dict(zip(column_names, row))  
                for row in cur.fetchall()] 
        
        return self._name, db
 


