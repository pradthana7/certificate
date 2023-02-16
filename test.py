import hashlib

data_list = []
index = -1

def sha_512(t):
    # join str before sha512
    joinstr = "".join(data_list[-1])
    print("joinstr>>>", joinstr)
    hash_data = hashlib.sha512(joinstr.encode())
    res = hash_data.hexdigest()
    print("The hexadecimal equivalent of SHA512 is : ",res)

    with open("Signature{}.txt".format(index),"w") as file:
        file.write(str(res))


while True:
    sname = input("Enter Name: ")
    sid = input("Enter sid: ")
    pname = input("Enter project name: ")
    exdate = input("date of experied: ")
    sc = input("score: ")

    index += 1
    # add new dats list to all data list
    new_data = [[sname,sid,pname,exdate,sc]]
    # extend  new_date to t: list
    data_list.extend(new_data)

    print("new_data",new_data)
    print("after append >>>", data_list)

    with open("Certificate.txt", "w") as file:
        file.write(str(data_list))
    
    sha_512(data_list)

    

    


