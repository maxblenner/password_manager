from base64 import encodebytes
from encodings import utf_8
import bcrypt
import hashlib


def genSalt(): #using bcrypt to generate a random salt
    salt = bcrypt.gensalt()
    return salt

def hashInput(userIn): #hashing input
    hashedPW = hashlib.md5(userIn).hexdigest().encode()
    return hashedPW

def checkPassword(userIn, storedPW, salt): #checks user input against stored salted password by salting the password with the same salt and comparing the results
    hashedIn = hashInput(userIn)
    saltedIn = hashedIn + salt
    
    if saltedIn == storedPW:
        print("Correct Password!")
        #print(saltedIn)
        return True
    else:
        print("Incorrect Password.")
        #print(saltedIn)
        return False

userIn = input(b"Enter password to be stored: ").encode() #hashing functionality requires string to be encoded

userSalt = genSalt()
hashedPW = hashInput(userIn)
encryptedPW =  hashedPW + userSalt

userIn = input(b"Enter password: ").encode()

checkPassword(userIn, encryptedPW, userSalt)




