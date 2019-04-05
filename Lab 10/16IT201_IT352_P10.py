from tkinter import *
from cyclic import *
from blind_signature import *
from choosen_ciphertext import *
def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
master.option_add('*font', ('verdana', 12))
master.title("Lab 10 assignment")
master.geometry("500x500")
Label(master,text='Click which program you want').pack()   


Button(master, text='Cyclic cipher attack', command=cyclic).pack(side=TOP,expand=YES)
Button(master, text='Blind signature attack', command=bs).pack(side=TOP,expand=YES)
Button(master,text='Choosen ciphertext attack',command=cct).pack(side=TOP,expand=YES)
mainloop( )