from tkinter import *
from tkinter import ttk, messagebox



import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import re



GUI = Tk()
GUI.title("My Certificate")
GUI.geometry("1000x700")

FONT30 = ("Angsana New", 30)
FONT20 = ("Angsana New", 20)

data_list = []
index = -1

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
    print("data_list",data_list)

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

####################GUI func###########################





















##############################################################

L = Label(GUI,text="Certificate Issuance Program", font=FONT30)
L.pack(pady=20)

L = Label(GUI,text="Student Name", font=FONT20)
L.pack()
v_sname = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_sname,font=FONT20)
E1.pack(pady=5)

L = Label(GUI,text="Student ID", font=FONT20)
L.pack()
v_sid = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_sid,font=FONT20)
E2.pack(pady=5)

L = Label(GUI,text="Project Name", font=FONT20)
L.pack()
v_pname = StringVar()
E3 = ttk.Entry(GUI,textvariable=v_pname,font=FONT20)
E3.pack(pady=5)

L = Label(GUI,text="Date Of Experied (YYYY-MM-DD)", font=FONT20)
L.pack()
v_exdate = StringVar()
E4 = ttk.Entry(GUI,textvariable=v_exdate,font=FONT20)
E4.pack(pady=5)

L = Label(GUI,text="Please enter a score between 60 and 100", font=FONT20)
L.pack()
v_sc = StringVar()
E5 = ttk.Entry(GUI,textvariable=v_sc,font=FONT20)
E5.pack(pady=5)
E5.bind("<Return>", Append) #press enter  will be submit

B1 = ttk.Button(GUI,text="submit", command=Append)
B1.pack(pady=30, ipadx=20, ipady=10)

v_result = StringVar()
result = ttk.Label(GUI,textvariable=v_result, foreground="green")




GUI.mainloop()