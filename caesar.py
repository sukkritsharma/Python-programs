from cs50 import get_string
import sys

if len(sys.argv) !=2:
    exit(1)

key = int(sys.argv[1])

text = get_string("plaintext: ")
print("ciphertext: ",end="")

for c in text:
    if c.islower():
        print(chr((ord(c) - ord('a') + key )%26 + ord('a')),end='')
    elif c.isupper():
        print(chr((ord(c) - ord('A') + key )%26 + ord('A')),end='')
    else:
        print(c,end='')
print()