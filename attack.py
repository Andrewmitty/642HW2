# /usr/bin/env python3
# CS 642 University of Wisconsin
#
# usage: python3 attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys
import Crypto.Cipher.AES
import hashlib

# Grab ciphertext from first argument
ciphertextWithTag = bytes.fromhex(sys.argv[1])

if len(ciphertextWithTag) < 16 + 16 + 32:
    print("Ciphertext is too short!")
    sys.exit(0)

iv = ciphertextWithTag[:16]
ciphertext = ciphertextWithTag[:len(ciphertextWithTag) - 32]
tag = ciphertextWithTag[len(ciphertextWithTag) - 32:]

#Find the position of the amount field in the plaintext message
# plaintext = Crypto.Cipher.AES.new(b"\x00"*16, Crypto.Cipher.AES.MODE_CBC, IV=iv).decrypt(ciphertext)
# amount_pos = plaintext.find(b"$")

#Modify the amount field to a more lucrative value
# new_amount = b"$9999.99"
# new_plaintext = plaintext[:amount_pos] + new_amount + plaintext[amount_pos+len(new_amount):]

plaintext = """AMOUNT: $  12.99
Originating Acct Holder: Alexa
Orgininating Acct #98166-20633

I authorized the above amount to be transferred to the account #51779-31226
held by a Wisc student at the National Bank of the Cayman Islands.
"""

new_plaintext = """AMOUNT: $1299.99
Originating Acct Holder: Alexa
Orgininating Acct #98166-20633

I authorized the above amount to be transferred to the account #51779-31226
held by a Wisc student at the National Bank of the Cayman Islands.
"""

# Recalculate the tag using the modified plaintext


# Construct the new ciphertext by encrypting the modified plaintext with the same key and IV
# cipher = Crypto.Cipher.AES.new(b'\x00' * 16, Crypto.Cipher.AES.MODE_CBC, IV=iv)
# new_ciphertext = cipher.encrypt(new_plaintext).hex()
# new_tag = hashlib.sha256(new_plaintext).hexdigest()

# new_ciphertext = new_iv.hex() + ciphertext.hex() + tag.hex()
ascii_plain_text = plaintext[:16].encode('ascii')
# ascii_plain_text = codecs.encode(ascii_plain_text, 'hex')
# print(ascii_plain_text)


E = ascii_plain_text ^ iv #xor to get E, followed steps from the stackoverflow article
#https://crypto.stackexchange.com/questions/85785/can-you-change-an-aes-encrypted-message-if-you-control-the-iv
print(E)

# Print the new encrypted message
print(iv.hex() + new_ciphertext + new_tag)
