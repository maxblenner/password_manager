from base64 import encodebytes
from encodings import utf_8
import bcrypt
import hashlib

def genSalt(): #using bcrypt to generate a random salt
    salt = bcrypt.gensalt()
    return salt

def hashInput(userIn): #hashing input
    hashed = hashlib.md5(userIn).hexdigest().encode()
    return hashed

def addHash(userIn, salt): #concatenate user in with salt    
    salted = userIn + salt 
    hashed = hashInput(salted.encode())
    return hashed.decode('ascii')

def checkPassword(userIn, storedPW, salt): #checks user input against stored salted password by salting the password with the same salt and comparing the results
    saltedIn = addHash(userIn, salt)
    
    if saltedIn == storedPW:
        print("Correct Password!")
        return True
    else:
        print("Incorrect Password.")
        return False

