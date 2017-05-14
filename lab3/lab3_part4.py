# Eric Xie hx8rc
from Crypto.Cipher import DES
import json

while True:
    key = input("Enter a key: ")
    if len(key) % 8 == 0:
        break
    else:
        key = input("Your key length must be a multiple of 8")
msg = input("Enter a message: ")
des = DES.new(key, DES.MODE_ECB)
cipher_text = des.encrypt(msg)
keyMessage = {key:cipher_text}
with open("secret.txt", "w") as f:
    f.write(json.dumps(keyMessage))
f.close()