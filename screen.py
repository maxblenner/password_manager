#import database file
from database_manager import addAcc, connectDatabase
from collections import ChainMap
# name = input("Enter Username: ")
# password = input("Enter Password: ")



class userAccount(object):
    """docstring for userAccount."""

    def __init__(self, name=None, password=None):
        super(userAccount, self).__init__()
        self._name = name
        self._password = password

    def userData(self):
        #fetch user data
        conn= connectDatabase()
        cur = conn.cursor()
        cur.execute("SELECT * FROM account")
        desc= cur.description
        column_names = [col[0] for col in desc]
        db= dict(ChainMap(*[dict(zip(column_names, row))  
                    for row in cur.fetchall()] ))        
        with open("userData.txt", 'a') as f:                    
                        for key, value in db.items(): 
                            f.write('%s:%s;' % (key, value))
        
        file = open("userData.txt", "r")
        return self._name,  file.read().strip("\n")
      
