#Eric Xie hx8rc
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC4


def secret_string(string, key):
    enc_data = key.encrypt(str.encode(string), 32)
    return enc_data


def encrypt_file(filename, key):
    key = str(key)
    keyObj = ARC4.new(key)
    enc_filename = str(filename) + ".enc"
    try:
        with open(filename, "rb") as in_file:
            with open(enc_filename, 'wb') as out_file:
                while True:
                    data = in_file.read()
                    if len(data) == 0:
                        break
                    else:
                        out_file.write(keyObj.encrypt(data))
    except FileNotFoundError:
        print("The specified file doesn't exist")
        return False
    return True
def decrypt_file(filename, key):
    key = str(key)
    if filename[-4:] != ".enc":
        print("Filename not in valid .enc format")
        return False
    keyObj = ARC4.new(key)
    dec_filename = "DEC_" + str(filename)[:-4]
    try:
        with open(filename, "rb") as in_file:
            with open(dec_filename, 'wb') as out_file:
                while True:
                    data = in_file.read()
                    if len(data) == 0:
                        break
                    else:
                        out_file.write(keyObj.decrypt(data))
    except FileNotFoundError:
        print("The specified file doesn't exist")
        return False
    return True

def test_string_enc():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    public_key = key.publickey()
    enc_msg = secret_string("hello", public_key)
    print(enc_msg)
    dec_msg = key.decrypt(enc_msg).decode("utf-8")
    print(dec_msg)

if __name__ == "__main__":
   test_string_enc()

