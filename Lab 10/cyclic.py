from tkinter import *
newwin=0
e1=0
e2=0
e3=0
e4=0
e5=0
def exp_modulo(a,b,N):
    result=1
    while b>0 :
        a=a%N
        if b%2==1 :
            result=result*a%N
        a=a*a
        b=b//2
    return result%N

def cyclic():
    global newwin,e1,e2,e3,e4,e5
    newwin = Tk()
    display = Label(newwin, text="Cyclic attack")
    display.grid(row=1,column=1)
    newwin.title("Cyclic attack")
    Label(newwin, text="Cipher text").grid(row=2)
    Label(newwin, text="N").grid(row=3)
    Label(newwin, text="e").grid(row=4)
    newwin.geometry("500x500")
    e1 = Entry(newwin)
    e2 = Entry(newwin)
    e3=Entry(newwin)
    e1.grid(row=2, column=1)
    e2.grid(row=3, column=1)
    e3.grid(row=4,column=1)
    
    
    Button(newwin, text='Submit', command=cyclic1).grid(row=5)
    Label(newwin, text="Plaintext is").grid(row=6)
    Label(newwin,text="encrypting plain text").grid(row=7)
    e4 = Entry(newwin)
    e4.grid(row=6,column=1)
    e5=Entry(newwin)
    e5.grid(row=7,column=1)
    newwin.mainloop()

def cyclic1():
    rows=6
    global newwin,e1,e2,e3,e5,e4
    f=open("Program5-Output-CyclicProgram5.txt",'w')
    ciphertext=int(e1.get())
    N=int(e2.get())
    e=int(e3.get())
    plaintext=0
    temp=ciphertext
    c=0
    
    while c==0 or temp!=ciphertext:
        c=c+1
        plaintext=temp
        
        temp=exp_modulo(temp,e,N)
        #print("cyclic No:",c,"intermediate cipher:",temp)
        #Label(newwin,text="cylic No."+str(c)+"intermediate cipher:"+str(temp)).grid(row=rows)
        #rows+=1
        print("cyclic No:",c,"intermediate cipher:",temp)
        #print(c)
    
    e4.insert(0,str(plaintext))
    rows=rows+1
    print("plaintext is: ",plaintext)
    print("plaintext is: ",plaintext,file=f)
    ciphertext=exp_modulo(plaintext,e,N)
    e5.insert(0,str(ciphertext))
    print("encrypting the plain text obtained: ",ciphertext)
    print("encrypting the plain text obtained: ",ciphertext,file=f)
    newwin.mainloop()    
if __name__ == "__main__":
    main()
    
