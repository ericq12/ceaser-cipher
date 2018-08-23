import string
import collections
mode = input("press e for encryption or d for decryption\n")
plaintext = input("enter your message or file (put ! in front of a filename)\n")
if(plaintext[0] == "!"):
    f = open(plaintext[1:], "r")
    plaintext=f.read()

def encrypt():
    #encrypt
    x = len(plaintext)
    shift = int(input("enter the shift or press 0 for a brute attack\n"))
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
    shift = int(input("enter the shift or press 0 for a brute attack\n"))
    x = len(plaintext)
    plainkey = collections.deque(string.ascii_lowercase)
    plainkey.rotate(shift)
    cipherkey = list(plainkey)
    plainkey.rotate(-shift)
    plainkey.append(" ")
    cipherkey.append(" ")
    if(shift == 0):
        while(shift < 27):
            plainkey.rotate(shift)
            cipherkey = list(plainkey)
            plainkey.rotate(-shift)
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
            shift = shift + 1
    else:
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
