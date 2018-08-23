import string
import collections
f = open("encryption.txt", "w")
f.write("")
f = open("decryption.txt", "w")
f.write("")
mode = input("Press e for encryption or d for decryption\n")
if(mode != "e" or "d"):
    print("Enter valid mode")
    mode = input("Press e for encryption or d for decryption\n")
plaintext = input("Enter your message or file (put ! in front of a filename)\n")
if(plaintext[0] == "!"):
    f = open(plaintext[1:], "r")
    plaintext=f.read()

def encrypt():
    #encrypt
    x = len(plaintext)
    shift = int(input("Enter the shift\n"))
    plainkey = collections.deque(string.ascii_lowercase)
    plainkey.rotate(-shift)
    cipherkey = list(plainkey)
    plainkey.rotate(shift)
    i = 0
    while (i < x):
        y = 0
        if(plaintext[i] == " "):
            f = open("encryption.txt", "a")
            f.write(" ")
            print(" ", end='')
            y = y + 1
            i = i + 1
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
    shift = int(input("Enter the shift or press 0 for a brute attack\n"))
    x = len(plaintext)
    plainkey = collections.deque(string.ascii_lowercase)
    plainkey.rotate(shift)
    cipherkey = list(plainkey)
    plainkey.rotate(-shift)
    brutefile = list(plainkey)
    brutefile.append("IGNORE")
    #bruteforce
    if(shift == 0):
        k = 0
        while(k < 26):
            f = open("shift"+brutefile[k]+".txt", "w")
            f.write("")
            k = k + 1
        k = 0
        while(shift < 26):
            plainkey.rotate(shift)
            cipherkey = list(plainkey)
            plainkey.rotate(-shift)
            i = 0
            while (i < x):
                y = 0
                if(plaintext[i] == " "):
                    f = open("shift"+brutefile[k]+".txt", "a")
                    f.write(" ")
                    print(" ", end='')
                    y = y + 1
                    i = i + 1
                while(plaintext[i] != plainkey[y]):
                    y = y + 1
                if(plaintext[i] == plainkey[y]):
                    encryption = cipherkey[y]
                    if(brutefile[k] != "IGNORE"):
                        f = open("shift"+brutefile[k]+".txt", "a")
                        f.write(encryption)
                        print(encryption, end='')
                i = i + 1
            print(" ")
            shift = shift + 1
            k = k + 1
    #shift decryption
    else:
        i = 0
        while (i < x):
            y = 0
            if(plaintext[i] == " "):
                f = open("decryption.txt", "a")
                f.write(" ")
                print(" ", end='')
                y = y + 1
                i = i + 1
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
