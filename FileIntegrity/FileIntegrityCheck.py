import os
import hashlib
hashes = []
files = os.listdir("ProtectedFiles")
stored_hashes = []
rounds = 0
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
    hash_content = hashfile.readlines()
    for hash in hash_content:
        stored_hashes.append(hash.strip("\n"))
    print(stored_hashes)
for file in files:
    if hashes[rounds] == stored_hashes[rounds]:
        print(f"{file} has passed integrity check")
    else:
        print(f"{file} has failed integrity check")
    rounds += 1