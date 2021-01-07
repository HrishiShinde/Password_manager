import random, hashlib, binascii, pyperclip, base64, os
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode

def enc_pass(sitepass, upass):

    #upass = upass.encode('utf-8')
    #key = urlsafe_b64encode(upass)

    sitepass = bytes(sitepass, 'utf-8')

    cyrpter = Fernet(upass)
    enc_pass = cyrpter.encrypt(sitepass) #encrypting
    print(enc_pass)

    dec_pass = cyrpter.decrypt(enc_pass) #decrypting
    print(dec_pass)

    return enc_pass

def dec_pass():

    
    pass

def pass_hash(upass):
    userpass = bytes(upass, 'utf-8')
    salt = bytes("BabyShark", 'utf-8')
    backend = default_backend()

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=backend)
    hashed_upass = kdf.derive(userpass)
    hashed_upass = base64.urlsafe_b64encode(hashed_upass)
    return hashed_upass
