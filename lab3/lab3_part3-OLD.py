# Eric Xie hx8rc
import json
with open("file_info.txt","r") as f:
    allLines = f.read()
    filelist = json.loads(allLines)
    lineNumbers = filelist[1]
    for key in lineNumbers.keys():
        with open(key, "r") as tempFile:
            length = len(tempFile.readlines())
            if lineNumbers[key] != length:
                print("Number of lines in", key,"differs from what was stored in file_info.txt")
        tempFile.close()
f.close()