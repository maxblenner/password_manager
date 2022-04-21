from os import path
from cryptography.fernet import Fernet



def create_key(filename,sf):
    
    sf.destroy()    
    filepath = filename
    key = Fernet.generate_key()
    # Creates a new file
    with open(filepath, 'wb') as f:
        f.write(key)

    
def load_key(key_file):    
    try:
        filename =  key_file 
        with open(filename, 'rb') as f:
            key = f.read()
            return key
        
    except:        
        print("No local key file found!, key created")        
        return None
    
def encrypt_password(password,key_file):    
    key = load_key(key_file)
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted.decode('ascii')

def decrypt_password(encrypted_pw,key_file):
    key = load_key(key_file).decode('ascii')   
    f = Fernet(key)    
    decrypted = f.decrypt(encrypted_pw)
    return decrypted.decode('ascii')
