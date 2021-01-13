import random, hashlib, binascii, pyperclip, base64, os
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode

def enc_pass(sitepass, uname):
    sitepass = bytes(sitepass, 'utf-8')

    key = pass_hash(uname)
    crypter = Fernet(key)
    enc_pass = crypter.encrypt(sitepass) #encrypting
    #print(enc_pass)

    return enc_pass

def dec_pass(uname, spass):
    key = pass_hash(uname)
    crypter = Fernet(key)
    dec_pass = crypter.decrypt(spass) #decrypting
    #print(dec_pass)
    
    return dec_pass

def pass_hash(upass):
    supposed_key = bytes(upass, 'utf-8')
    salt = bytes("BabyShark", 'utf-8')
    backend = default_backend()

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=backend)
    hashed_upass = kdf.derive(supposed_key)
    hashed_upass = base64.urlsafe_b64encode(hashed_upass)

    return hashed_upass
