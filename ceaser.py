import string
import collections
mode = input("press e for encryption or d for decryption\n")
plaintext = input("enter your message or file (put ! in front of a filename)\n")
if(plaintext[0] == "!"):
    f = open(plaintext[1:], "r")
    plaintext=f.read()
shift = int(input("enter the shift\n"))

def encrypt():
    #encrypt
    x = len(plaintext)
    plainkey = collections.deque(string.ascii_lowercase)
    plainkey.rotate(-shift)
    cipherkey = list(plainkey)
    plainkey.rotate(shift)
    plainkey.append(" ")
    cipherkey.append(" ")
    i = 0
    while (i < x):
        y = 0
        while(plaintext[i] != plainkey[y]):
            y = y + 1
        if(plaintext[i] == plainkey[y]):
            encryption = cipherkey[y]
            f = open("encryption.txt", "a")
            f.write(encryption)
            print(encryption, end='')
        i = i + 1
    print(" ")

def decrypt():
    #decrypt
    x = len(plaintext)
    plainkey = collections.deque(string.ascii_lowercase)
    plainkey.rotate(shift)
    cipherkey = list(plainkey)
    plainkey.rotate(-shift)
    plainkey.append(" ")
    cipherkey.append(" ")
    i = 0
    while (i < x):
        y = 0
        while(plaintext[i] != plainkey[y]):
            y = y + 1
        if(plaintext[i] == plainkey[y]):
            encryption = cipherkey[y]
            f = open("decryption.txt", "a")
            f.write(encryption)
            print(encryption, end='')
        i = i + 1
    print(" ")

if(mode == "e"):
    encrypt()

if(mode == "d"):
    decrypt()
