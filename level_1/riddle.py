##Level 1

#ToDo: Find the XOR key used to encrypt the message
#Hint: XOR is not encryption

key = None
if(key != None):
    with open("data.bin", "rb") as f:
        decoded = bytes(b ^ key for b in f.read())

try:
    text = decoded.decode("ascii")
except:
    print("Wrong key.")
    exit(1)

if not text.startswith("KEY1="):
    print("Wrong key.")
    exit(1)

print("\n✔ Decrypted:\n")
print(text)
