# /usr/bin/env python3
# CS 642 University of Wisconsin
#
# usage: python3 attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys
import hashlib

# Grab ciphertext from first argument
ciphertextWithTag = bytes.fromhex(sys.argv[1])

if len(ciphertextWithTag) < 16 + 16 + 32:
    print("Ciphertext is too short!")
    sys.exit(0)

iv = ciphertextWithTag[:16]
#adding 16 to skip iv in ciphertext
ciphertext = ciphertextWithTag[16:len(ciphertextWithTag) - 32]
tag = ciphertextWithTag[len(ciphertextWithTag) - 32:]

# changing the IV
new_val = bytearray("AMOUNT:$ 9999.99", "utf-8")
old_val = bytearray("AMOUNT: $  12.99", "utf-8")

for i in range(len(new_val)):
    new_val[i] = new_val[i] ^ old_val[i]
    new_val[i] = new_val[i] ^ iv[i]

iv = bytes(new_val)

new_plaintext = \
    """AMOUNT:$ 9999.99
Originating Acct Holder: Alexa
Orgininating Acct #98166-20633

I authorized the above amount to be transferred to the account #51779-31226 
held by a Wisc student at the National Bank of the Cayman Islands.
"""

tag = hashlib.sha256(new_plaintext.encode()).hexdigest()
# you can change the print content if necessary
print(iv.hex() + ciphertext.hex() + tag)
