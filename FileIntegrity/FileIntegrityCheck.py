import hashlib
with open("fileIntegrity.txt", "r+") as integrityfile:
    file_content = integrityfile.read()
    file_encoded = file_content.encode()
    fileHash = hashlib.sha256(file_encoded).hexdigest()
with open ("fileHash.txt", "r+") as hashfile:
    if len(hashfile.readline())==0:
        hashfile.write(fileHash)
    hashfile.seek(0)
    if fileHash == hashfile.read():
        print("File integrity check passed")
    else:
        print("File integrity check failed")