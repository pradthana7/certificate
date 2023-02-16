import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

data_list = []
index = -1


def SHA_512(lst):
    # join str before sha512
    joinstr = " ".join(data_list)
    # print("joinstr>>>", joinstr)
    hashed_string = hashlib.sha512(joinstr.encode('utf-8')).digest()

    with open("Certificate{}.txt".format(index), "w") as file:
        file.write(str(data_list))

    data_list.clear()

    return hashed_string


def Signature(msg):
    # Load private key previouly generated
    with open("privatekey.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=b'mypassword',
        )

    # signing
    signature = private_key.sign(
        msg,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA512()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA512()
    )

    with open("Signature{}.txt".format(index), "w") as file:
        file.write(str(signature))


while True:
    index += 1

    sname = input("Enter Name: ")
    data_list.append(sname)

    sid = input("Enter sid: ")
    data_list.append(sid)

    pname = input("Enter project name: ")
    data_list.append(pname)

    exdate = input("date of experied: ")
    data_list.append(exdate)

    sc = input("score: ")
    data_list.append(sc)

    # call func
    msg = SHA_512(data_list)
    Signature(msg)
