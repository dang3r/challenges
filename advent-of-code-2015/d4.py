import hashlib

input_text = "iwrupvqb"

i = 0
while True:
    hash = hashlib.md5(f"{input_text}{i}".encode()).hexdigest()
    if hash.startswith("000000"):
        print(i)
        break
    i += 1
