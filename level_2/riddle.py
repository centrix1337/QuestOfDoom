import hashlib

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

with open("hashes.txt", "r", encoding="utf-8") as f:
    targets = [line.strip().lower() for line in f if line.strip()]

with open("dictionary.txt", "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]


#ToDo: Find the words associated with the 2 given hash values
#Keep the order of hashes.txt
solution_words = {"",""}
key2 = "".join(solution_words).upper()

print(f"\nKEY2={key2}")
