




def solve(t):
   return hash(t)


t = [("pradthana","b632213","algorithm","2022/02/01",100)]



while True:
    

    sname = input("Enter Name: ")
    sid = input("Enter sid: ")
    pname = input("Enter project name: ")
    exdate = input("date of experied: ")
    sc = input("score: ")


    new_item = [(sname,sid,pname,exdate,sc)]


    t.extend(new_item)

    print("new_item",new_item)
    print("after append >>>", t)

    print(solve(t[-2]))

    with open("listFile.txt", "w") as file:
        file.write(str(t))