from tkinter import *
from tkinter import ttk, messagebox
import os
import csv

import hashlib
import re
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from datetime import date


GUI = Tk()
GUI.title("MyCertificate-B6322113")
GUI.geometry("1000x700")

FONT30 = ("Angsana New", 30)
FONT20 = ("Angsana New", 20)

data_list = []
index = -1
directory = "./"
count = 0
############################config tab#########################
Tab =ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)

icon_tab1 = PhotoImage(file="tab1.png")
icon_tab2 = PhotoImage(file="tab2.png")

Tab.add(T1,text="signature",image=icon_tab1,compound="left")
Tab.add(T2,text="verify",image=icon_tab2,compound="left")

####################signature func###########################

def Append(event=None):
    global index
    index += 1

    sname = v_sname.get()
    data_list.append(sname)

    sid = v_sid.get()
    data_list.append(sid)

    pname = v_pname.get()
    data_list.append(pname)

    exdate = v_exdate.get()
    data_list.append(exdate)

    sc = v_sc.get()
    data_list.append(sc)
    
    data = [sid,sname,pname]
    with open("data.csv","a",newline="",encoding="utf-8") as file:
        fw = csv.writer(file)
        fw.writerow(data)

    SHA_512(data_list)



def SHA_512(data_list):
    # join str before sha512
    joinstr = "".join(data_list)
    print("joinstr>>>", joinstr)
    hashed_string = hashlib.sha512(joinstr.encode('utf-8')).digest()
    print("hashed_string>>>", hashed_string)

    with open("Certificate{}.txt".format(index), "w") as file:
        for i in range(4):
            file.write('{}\n'.format(data_list[i]))
        file.write(data_list[-1])

    data_list.clear()

    # return hashed_string
    Signature(hashed_string)


def Signature(msg):
    # Load private key previouly generated 
    with open('private_key.pem', 'rb') as file:
        private_pem = file.read()
        private_key = load_pem_private_key(private_pem, password=None)
        print("private_key",private_key)

    # signing
    signature = private_key.sign(
        msg,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA512()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA512()
    )

    with open("Signature{}.txt".format(index), "wb") as file:
        file.write(signature)

    text = "Project certificate has been issued successfully."
    # v_result.set(text)
    messagebox.showinfo("success", text)

    ###############clear textbox###################
    v_sname.set("")
    v_pname.set("")
    v_exdate.set("")
    v_sc.set("")
    v_sid.set("")
    v_result.set("")
    ###############fix cursor at E1################
    E1.focus()

##############################Tab1################################

L = Label(T1,text="Certificate Issuance Program", font=FONT30)
L.pack(pady=20)

L = Label(T1,text="Student Name", font=FONT20)
L.pack()
v_sname = StringVar()
E1 = ttk.Entry(T1,textvariable=v_sname,font=FONT20)
E1.pack(pady=5)

L = Label(T1,text="Student ID", font=FONT20)
L.pack()
v_sid = StringVar()
E2 = ttk.Entry(T1,textvariable=v_sid,font=FONT20)
E2.pack(pady=5)

L = Label(T1,text="Project Name", font=FONT20)
L.pack()
v_pname = StringVar()
E3 = ttk.Entry(T1,textvariable=v_pname,font=FONT20)
E3.pack(pady=5)

L = Label(T1,text="Date Of Experied (YYYY-MM-DD)", font=FONT20)
L.pack()
v_exdate = StringVar()
E4 = ttk.Entry(T1,textvariable=v_exdate,font=FONT20)
E4.pack(pady=5)

L = Label(T1,text="Please enter a score between 60 and 100", font=FONT20)
L.pack()
v_sc = StringVar()
E5 = ttk.Entry(T1,textvariable=v_sc,font=FONT20)
E5.pack(pady=5)
E5.bind("<Return>", Append) #press enter  will be submit

B1 = ttk.Button(T1,text="submit", command=Append)
B1.pack(pady=30, ipadx=20, ipady=10)

v_result = StringVar()
result = ttk.Label(T1,textvariable=v_result, foreground="green")


##############################Tab2################################

header = ["index", "studentID","project",]
hwidth = [100,200,400]

table = ttk.Treeview(T2, columns=header,show="headings", height=20)
table.pack()

style = ttk.Style()
style.configure("Treeview.Heading", font=FONT20)
style.configure("Treeview",font=FONT20,rowheight=30)

for h,w in zip(header,hwidth):
    table.column(h,width=w)
    table.heading(h,text=h)


##########################verify###################################
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


#########################################data in table###################################################


#insert data to table




GUI.mainloop()