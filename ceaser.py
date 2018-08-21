import string
import collections
mode = input("press e for encryption or d for decryption\n")
if(mode == "e"):
    #encrypt
    plaintext = input("enter your plaintext\n")
    x = len(plaintext)
    shift = int(input("enter the shift\n"))
    plainkey = collections.deque(string.ascii_lowercase)
    plainkey.rotate(-shift)
    cipherkey = list(plainkey)
    plainkey.rotate(shift)
    plainkey.append(" ")
    cipherkey.append(" ")
    print(cipherkey)
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

if(mode == "d"):
    #decrypt
    plaintext = input("enter the ciphertext\n")
    x = len(plaintext)
    shift = int(input("enter the shift\n"))
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
