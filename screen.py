#import database file

class userAccount(object):
    """docstring for userAccount."""

    def __init__(self, name=None, password=None):
        super(userAccount, self).__init__()
        self._name = name
        self._password = password

    def userData(self):
        #fetch user data
        file = open("userData.txt", "r")
        return self._name,  file.read().strip("\n")
