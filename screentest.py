#import database file
from database_manager import findData
from collections import ChainMap
# name = input("Enter Username: ")
# password = input("Enter Password: ")
import time



class userAccount(object):
    """docstring for userAccount."""

    def __init__(self, userID):
        super(userAccount, self).__init__()
        self.__userID = userID
        

    def fetchData(self):
        #fetch user data
        print("fetching Data...")
        time.sleep(1)
        return findData(str(self.__userID))
        #with open("fetchData.txt", 'w') as f:
        #        for item in pw_db:                      
        #               f.write("%s\n" % item)
        
        
       
