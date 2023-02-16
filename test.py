data_list = ["prad","B6666666","projectname","2002-02-02","87"]

with open("test.txt", "w") as f:
    for i in range(4):
        f.write('{}\n'.format(data_list[i]))
    f.write(data_list[-1])