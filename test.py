
import hashlib



def sha_512(t):
    return hash(t)


t = [["pradthana","b632213","algorithm","2022/02/01",100]]



while True:


    sname = input("Enter Name: ")
    sid = input("Enter sid: ")
    pname = input("Enter project name: ")
    exdate = input("date of experied: ")
    sc = input("score: ")


    new_item = [[sname,sid,pname,exdate,sc]]


    t.extend(new_item)

    print("new_item",new_item)
    print("old list t>>>",t)
    print("after append >>>", t)


    with open("listFile.txt", "w") as file:
        file.write(str(t))


    # join str before sha512
    joinstr = "".join(t[-1])
    print("joinstr>>>", joinstr)
    res = hashlib.sha512(joinstr.encode())
    print("The hexadecimal equivalent of SHA512 is : ",res.hexdigest())

