from cryptography import Fernet as fernet
import string

# The Code from the Cryptography branch will be deleted; it is only here for inspiration while making our own function.
# The Code for Fernet is encoded in UTF-8 and as such we should try to create an encoding function first.

def write_key():
    # This is a key to our encrpyted item
    key = fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    # This loads the key for encryption from the key.key directory
    return open('key.key', 'rb').read()

write_key() # this creates the folder for our encryption key

key = load_key() # loads the key for our encrypted function

f = fernet(key)
message = input('Paste data to encrypt.').encode() # this encode method uses UTF-8 by default.

encrypted = f.encrypt(message) # this encrypts the message to be decrypted later.

decrypted = f.decrypt(encrypted) # this decrypts whatever the input is.