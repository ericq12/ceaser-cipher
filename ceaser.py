import string
import collections

#encrypt
plaintext = input("enter your message\n")
x = len(plaintext)
shift = int(input("enter cipher\n"))
plainkey = collections.deque(string.ascii_lowercase)
plainkey.rotate(-shift)
cipherkey = list(plainkey)
plainkey.rotate(shift)
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
