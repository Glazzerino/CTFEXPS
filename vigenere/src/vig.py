import re
# Vigenere Cipher proof-of-concept

# Vigenere Cipher is resistant against frequency analyzers
m = input("Enter message: ").upper()
m = m.replace(" ", "")
k = input("Enter key: ").upper()
# Input check
def check_input(inp):
    dirty = re.search("\W|\d", inp)
    if dirty:
        print("bad input! letters only please")
        exit()
#Wrap any given index to the key 
def k_char(k: str, index: int):
    return k[index % len(k)]

# Trying out 1:1 key to message
ans = ""
for i in range(0, len(m)):
    ans += k_char(k, i)
print("masked message: " + ans)

ciphertext = ""

for i in range(0, len(m)):
    c_ord = (ord(m[i]) + ord(k_char(k, i))) % 26
    ciphertext += chr(c_ord+65)

print("Ciphertext: " + ciphertext)

# Decoding
decoded = ""
for i in range(0, len(ciphertext)):
    c = (ord(ciphertext[i]) - ord(k_char(k, i))) % 26
    decoded += chr(c+65)
print(decoded)

