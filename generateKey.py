from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA


##########################GENERATE CERTIFICATE PAIR########################

new_key = RSA.generate(2048)

private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")

with open("privatekey.pem", "wb") as file:
    file.write(private_key)

with open("publicKey.pem", "wb") as file:
    file.write(public_key)
