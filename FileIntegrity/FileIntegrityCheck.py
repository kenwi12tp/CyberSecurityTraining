import os
import hashlib
hashes = []
files = os.listdir("ProtectedFiles")
print(files)

for file in files:
    with open(f"ProtectedFiles/{file}", "r+") as file:
        file_content = file.read()
        file_encoded = file_content.encode()
        fileHash = hashlib.sha256(file_encoded).hexdigest()
        hashes.append(fileHash)
print(hashes)
with open ("fileHash.txt", "r+") as hashfile:
    for hash in hashes:
        if len(hashfile.readline())==0:
            hashfile.write(hash)
            hashfile.write("\n")
    hashfile.seek(0)
    for file in files:
        if hashfile.readlines() == hashes:
            print(f"{file} has passed integrity check")
        else:
            print(f"{file} has failed integrity check")
