from cryptography.fernet import Fernet


directory = "C:\\Users\\furka\\Desktop\\"

def create_key(filename):    
    #path = input("Put path: ")
    #os.mkdir(path)
   

    # get fileName from user
    filepath = directory + filename + '.txt'

    key = Fernet.generate_key()

    # Creates a new file
    with open(filepath, 'wb') as f:
        f.write(key)

    
def load_key():
    try:
        filename =  input("Enter a filename without extensions: ") + '.txt' 
        with open(directory+filename, 'rb') as f:
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
    return decrypted.decode('ascii')

#new_user = True

#if new_user == True: 
#    key = None

#if load_key() == None: 
#    create_key()

#key = load_key()

#arbitrary code to test if functions are working
#userIn = input("Enter something to be hashed: ")
#encrypted = encrypt_password(userIn.encode())
#print(encrypted)
#print(decrypt_password(encrypted))


#7DXGEcBBW304_l61kLB8wCpauWoRzoMhAkXe82I4pTM=
#ppsfSihZqVGtU-xnry4eMQ8P34n0-QatwrkGUfLOHrE=
#ppsfSihZqVGtU-xnry4eMQ8P34n0-QatwrkGUfLOHrE=


