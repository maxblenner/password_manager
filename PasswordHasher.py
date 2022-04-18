from cryptography.fernet import Fernet

<<<<<<< Updated upstream
def create_key():
=======

directory = "C:\\Users\\furka\\Desktop\\Keyfiles\\"

def create_key(filename):    
    #path = input("Put path: ")
    #os.mkdir(path)
   

    # get fileName from user
    filepath = directory + filename + '.txt'

>>>>>>> Stashed changes
    key = Fernet.generate_key()
    with open("userKey.txt", 'wb') as f:
        f.write(key)
    
def load_key():
    try: 
        with open("userKey.txt", 'rb') as f:
            key = f.read()
            return key
    except: 
        print("No local key file found!, key created")
        return None
    
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(password)
    return(encrypted)

def decrypt_password(encrypted_pw):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_pw)
    return(decrypted)

new_user = True

if new_user == True: 
    key = None

if load_key() == None: 
    create_key()

#key = load_key()

#arbitrary code to test if functions are working
userIn = input("Enter something to be hashed: ")
encrypted = encrypt_password(userIn.encode())
print(encrypted)
print(decrypt_password(encrypted))


#7DXGEcBBW304_l61kLB8wCpauWoRzoMhAkXe82I4pTM=
#ppsfSihZqVGtU-xnry4eMQ8P34n0-QatwrkGUfLOHrE=
#ppsfSihZqVGtU-xnry4eMQ8P34n0-QatwrkGUfLOHrE=