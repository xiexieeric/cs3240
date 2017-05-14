# Eric Xie hx8rc
import os
import json
filelist = []
linesDict = {}
for item in os.listdir():
    if not os.path.isdir(item):
        with open(item,"r") as f:
            numLines = len(f.readlines())
            linesDict[item] = numLines
        f.close()
filelist.append(os.getcwd())
filelist.append(linesDict)
with open("file_info.txt","w") as f:
    f.write(json.dumps(filelist, indent=4))
f.close()