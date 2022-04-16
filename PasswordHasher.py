from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    with open("userKey.txt", 'wb') as f:
        f.write(key)
    
def load_key():
    with open("userKey.txt", 'rb') as f:
        key = f.read()
        return key

def encrypt_password(key, password):
    f = Fernet(key)
    encrypted = f.encrypt(password)
    return(encrypted)

def decrypt_password(key, encrypted_pw):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_pw)
    return(decrypted)

new_user = True

if new_user == True: 
    key = None

if key == None: 
    create_key()

key = load_key()

#arbitrary code to test if functions are working
userIn = input("Enter something to be hashed: ")
encrypted = encrypt_password(key, userIn.encode())
print(encrypted)
print(decrypt_password(key,encrypted))


