#basic program that hashes strings

from encodings import utf_8
import bcrypt

userIn = input(b"Enter something to be hashed: ").encode('utf_8') #bcrypt requires byte strings and bcrypt.hashpw requires utf_8 encoding

hashedPW = bcrypt.hashpw(userIn,bcrypt.gensalt())

print(hashedPW)





