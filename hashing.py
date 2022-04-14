#basic program that hashes strings

from encodings import utf_8
import bcrypt

def hashPassword(userIn):
    hashedPW = bcrypt.hashpw(userIn,bcrypt.gensalt())
    return hashedPW

def checkPassword(userIn): 
    if bcrypt.checkpw(userIn,hashedPW):
        print("Correct Password")
    else:
        print("Incorrect Password")

userIn = input(b"Enter something to be hashed: ").encode('utf_8') #bcrypt requires byte strings and bcrypt.hashpw requires utf_8 encoding
hashedPW = hashPassword(userIn)

checkPassword(userIn)

print(hashedPW)





