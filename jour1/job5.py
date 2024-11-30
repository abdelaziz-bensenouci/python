#1er solution
import string
print(string.ascii_lowercase[::-1])

#2eme solutions
for lettre in range(ord('z'), ord('a') - 1, -1):
    print(chr(lettre), end=' ')

#3eme solution
chaine_reverse = "zyxwvutsrqponmlkjihgfedcba"
print(chaine_reverse)