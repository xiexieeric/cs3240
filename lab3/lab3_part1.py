# Eric Xie hx8rc
from Crypto.Hash import SHA256
accounts = {}
while True:
    username = input("Register a username: ")
    password = str.encode(input("Password: "))
    hexpw = SHA256.new(password).hexdigest()
    if password == b"":
        break
    accounts[username] = hexpw
while True:
    u = input("Username: ")
    p = str.encode(input("Password: "))
    hexp = SHA256.new(p).hexdigest()
    if u not in accounts:
        print("User not found")
        continue
    if accounts[u] == hexp:
        print("Login succeeds")
    else:
        print("Login fails")