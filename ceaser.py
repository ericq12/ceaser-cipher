import string
import collections
mode = input("press e for encryption or d for decryption\n")
plaintext = input("enter your message\n")
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
            print(encryption, end='')
        i = i + 1
    print(" ")

def decrypt():
    #decrypt
    # plaintext = input("enter the ciphertext\n")
    x = len(plaintext)
    # shift = int(input("enter the shift\n"))
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
            print(encryption, end='')
        i = i + 1
    print(" ")

if(mode == "e"):
    encrypt()

if(mode == "d"):
    decrypt()
