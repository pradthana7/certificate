import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import date

with open("test.txt", "r") as f:
    data_list_without_newline= f.read().split("\n")
    print("data_list_without_newline>>>",data_list_without_newline)

joinstr_fu = "".join(data_list_without_newline)
print("joinstr_fu>>>",joinstr_fu)
print("data_list_without_newline[3]>>>",data_list_without_newline[3])
hashed_string_read = hashlib.sha512(joinstr_fu.encode('utf-8')).digest()
print("hashed_string_read>>>",hashed_string_read)



data = ["prad","B6666666","projectname","2002-02-02","87"]
joinstr = "".join(data)
print("joinstr>>>",joinstr)
hashed_string_write = hashlib.sha512(joinstr.encode('utf-8')).digest()

print("hashed_string_write>>>",hashed_string_write)
