import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from datetime import date


def Verification(ver_index):
    with open("publicKey.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
        )
        print("public_key_fu>>>", public_key)

    with open("Certificate{}.txt".format(ver_index), "r") as file:
        list_certificate = file.read().split("\n")

    with open("Signature{}.txt".format(ver_index), "rb") as file:
        signature = file.read()  # digest2

    # check date of expired
    today = str(date.today())
    date_of_expired = list_certificate[3]

    print("today", date.today())

    if date_of_expired <= today:
        print("expired")
        exit()
    else:
        print("date of expired:", date_of_expired)

    try:
        # hash certificate in order to get Digest 1
        # error

        joinstr = "".join(list_certificate)
        digest1 = hashlib.sha512(joinstr.encode('utf-8')).digest()
        print("hashed_string>>>", digest1)

        print("joinstr>>>", joinstr)
        print("digest1>>>", digest1)
        # error
        print("public_key>>>", public_key)
        public_key.verify(
            signature,
            digest1,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA512()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA512()
        )
        print("you love me!")

    except:

        print("you")
        # print("digest2>>>", digest2)


Verification(0)

# print("Your Digital Signature Is Valid")
# print("Your Digital Signature Is Invalid")
