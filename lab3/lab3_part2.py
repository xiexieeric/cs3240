# Eric Xie hx8rc
import os
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

filelist = []
fileHashes = {}
for item in os.listdir():
    if not os.path.isdir(item):
        fileHashes[item] = get_file_checksum(item)
filelist.append(os.getcwd())
filelist.append(fileHashes)
with open("file_info.txt","w") as f:
    f.write(json.dumps(filelist, indent=4))
f.close()

#hi