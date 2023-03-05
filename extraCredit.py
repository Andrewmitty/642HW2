import hashlib
import time

# read file crackstation-human-only.txt and turn each line into a list
f = open("crackstation-human-only-8+.txt", "r")

content = f.readlines()
f.close()
print(content[0])
# content = [x.strip() for x in content]

print("starting")

targetHash = "fdd2a52969ff2cab2c2653e5cc7129a70b0cad398ea3ff44bf700bb0cd168d8b5c080c90b9281f04993b05895705229c3a5261e20f8a453369b81efd4f9040b6"
username = "bucky"
salt = "0719173488"
start = time.time()

# loop through each line in the list
for i in content:
    # hash each line
    msg = f"bucky,{i}"
    h = hashlib.scrypt(password=msg.encode(), salt=salt.encode(), n=16, r=32, p=1)
    # if the hash is equal to the target hash, print the password
    # print(h.hex(),end='\n')
    if h == targetHash:
        print(i)
        break

print((time.time() - start) * 65000000 / 60)
