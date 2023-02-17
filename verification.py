import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from datetime import date


def Verification(ver_index):
    with open('public_key.pem', 'rb') as file:
        public_pem = file.read()
        public_key = load_pem_public_key(public_pem)
        

    with open("Certificate{}.txt".format(ver_index), "r") as file:
        list_certificate = file.read().split("\n")

    with open("Signature{}.txt".format(ver_index), "rb") as file:
        signature = file.read()  # digest2

    # check date of expired
    today = str(date.today())
    date_of_expired = list_certificate[3]

    # print("today", date.today())

    if date_of_expired <= today:
        print("expired")
        exit()
    else:
        print("date of expired:", date_of_expired)

    try:
        # hash certificate in order to get Digest 1
        joinstr = "".join(list_certificate)
        digest1 = hashlib.sha512(joinstr.encode('utf-8')).digest()

        print("hashed_string>>>", digest1)
        print("joinstr>>>", joinstr)
        print("digest1>>>", digest1)

        public_key.verify(
            signature,
            digest1,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA512()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA512()
        )
        print("your signature is valid")

    except:

        print("your signature is invalid")




Verification(2)


