# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:16:28 2021

@author: siaaa013
"""


from cryptography.fernet import Fernet
import os
from stat import S_IREAD
from pathlib import Path
fLoc = input('Please write down the path to your file.')
fileloc = fLoc
fileName = Path(fLoc).name
key = Fernet.generate_key()
with open("ENCKEY.key", "w") as EncKey:
    EncKey.write(key)
os.chmod("ENCKEY.key", S_IREAD)
f = Fernet(key)
with open(fileloc, 'r') as OGFile:
    Og = OGFile
encrypt = f.encrypt(Og)
with open(fileName, 'w') as EncryptedFile:
    EncryptedFile.write(encrypt)