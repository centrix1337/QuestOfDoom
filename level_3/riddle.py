#There is also a riddle here

import hashlib

EXPECTED = "1f92e8b29719417f70b21272b85bcf40e9198d33e6da8b8cc93f2e74cf2a4b94"
MAGIC = "07f99fc746c8f1a335af42c179f7f43d4e4d162bf2faa02b0aeff85b4de6207d"

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def check_keys(keys: list[str]):
    key_string = ""
    for key in keys:
        key_string += key
    if sha256_hex(key_string) == EXPECTED:
        print("\nDecrypting...\n")
        with open("art.txt", "r", encoding="utf-8") as f:
            print(f.read())
    elif sha256_hex(key_string) == MAGIC:
        print("\nDecrypting final...\n")
        with open("final.enc", "rb") as f:
            enc = f.read()
            key = key_string.encode("utf-8")
            k = hashlib.sha256(key).digest()[0]
            plain = bytes(b ^ k for b in enc)
            print(plain.decode())


    else:
        print("\nKey is not correct")



#ToDo: Input KEY1 and KEY2 into this method

check_keys(["",""])








