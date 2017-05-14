# Eric Xie hx8rc
import json
from Crypto.Hash import MD5


def get_file_checksum(filename):
    h = MD5.new()
    chunk_size = 8192
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

with open("file_info.txt","r") as f:
    allLines = f.read()
    filelist = json.loads(allLines)
    fileHashes = filelist[1]
    for key in fileHashes.keys():
        if fileHashes[key] != get_file_checksum(key):
            print(key,"has been modified")
f.close()