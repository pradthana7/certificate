from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


gen_new_rsa = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

private_key = gen_new_rsa.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.PKCS8,
   encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
)

with open("privatekey.pem", "wb") as file:
    file.write(private_key)


public_key = gen_new_rsa.public_key().public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("publicKey.pem", "wb") as file:
    file.write(public_key)

