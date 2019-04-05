from tkinter import *
p=0
q=0
plaintext=0
r=0
e=0
e4=0
e5=0
import sys
class TeeFile(object):
    def __init__(self,*files):
        self.files = files
    def write(self,txt):
        for fp in self.files:
            fp.write(txt)

def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient
        if m==0 :
            return -1 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x 
def cct():
    global newwin,p,q,r,e,plaintext,e4,e5
    newwin = Tk()
    display = Label(newwin, text=" Choosen Cipher attack")
    display.grid(row=1,column=1)
    newwin.title("Choosen Cipher attack")
    Label(newwin, text="Cipher is").grid(row=2)
    Label(newwin, text="p").grid(row=3)
    Label(newwin, text="q").grid(row=4)
    Label(newwin, text="e").grid(row=5)
    Label(newwin, text="r").grid(row=6)
    newwin.geometry("500x500")
    plaintext = Entry(newwin)
    p = Entry(newwin)
    q=Entry(newwin)
    e=Entry(newwin)
    r=Entry(newwin)
    plaintext.grid(row=2, column=1)
    p.grid(row=3, column=1)
    q.grid(row=4,column=1)
    e.grid(row=5,column=1)
    r.grid(row=6,column=1)

    Button(newwin, text='Submit', command=choosen_ciphertext_attack).grid(row=7)
    
    
    newwin.mainloop()

def choosen_ciphertext_attack():
    global p,q,r,e,plaintext,e4,e5
    rows=8
    f=open("Program-7.output.txt","w")
    plaintext=plaintext.get()
    print("Plaintext is :",plaintext,file=f)
    p=int(p.get())
    print("p:",p,file=f)
    q=int(q.get())
    print("q:",q,file=f)
    N=p*q
    print("N:",N,file=TeeFile(sys.__stdout__,f))
    e=int(e.get())
    print("e:",e,file=f)
    phi=(p-1)*(q-1)
    d=modInverse(e,phi)
    
    if d==-1:
        Label(newwin, text="Plain text got after choosen ciphertext attack").grid(row=rows)
        e4 = Entry(newwin)
        e4.insert(0,"No private key d present ,exiting")
        print("No private key d present ,exiting",file=TeeFile(sys.__stdout__,f))
        
        return -1

    #determining block size
    M=hex(ord(plaintext[0])).split('x')[1]
    i=0
    N_bin_len=len(bin(N).split('b')[1])
    while i < N_bin_len:
        i=i+8
    if i!=8:
        block_size=(i-8)//8
    else:
        block_size=1

    if len(plaintext)%block_size!=0 :
    	plaintext=plaintext + ' '*(block_size-(len(plaintext)%block_size))
    
    r=int(r.get())
    print("r:",r,file=f)
    print("private key d is",d,file=TeeFile(sys.__stdout__,f))
    r_inverse=modInverse(r,N)
    print("r_inverse is ",r_inverse,file=TeeFile(sys.__stdout__,f))
    count=1
    # while r_inverse==-1 and count!=3:
    #     r=int(input("enter the value of r\n"))
    #     r_inverse=modInverse(r,N)
    #     count=count+1

    if r_inverse==-1 :
        Label(newwin, text="Plain text got after choosen ciphertext attack").grid(row=rows)
        e4 = Entry(newwin)
        e4.insert(0,"No r inverse exists present ,exiting")
        print("exiting",file=TeeFile(sys.__stdout__,f))
        return -1
    M=''
    Message=''
    plaintext_f=''
    print("No.of blocks ",len(plaintext)/block_size,file=TeeFile(sys.__stdout__,f))
    

    print("Blocksize in bits is ",block_size*8,file=TeeFile(sys.__stdout__,f))
    
    for i in range(0,len(plaintext),block_size):
        M=''
        for j in range(block_size):
            M=M+hex(ord(plaintext[i+j])).split('x')[1]
        print("\n------------------------------------",file=TeeFile(sys.__stdout__,f))
        print("block ",i//block_size,file=TeeFile(sys.__stdout__,f))
        
        M_hex=M
        M=int(M,16)
        
        # C=pow(M,e,N)
        # print("ciphertext in decimal:",C,file=TeeFile(sys.__stdout__,f))
        # M_actual_sign=hex(C).split('x')[1]
        # Sign_block=''

        # for p in range(0,len(M_actual_sign),2):
        #     Sign_block=Sign_block+chr(int(M_actual_sign[p:p+2],16))
        # print("cipher in acii ",Sign_block)
        C_dash=(M*pow(r,e))%N

        C_decrypted=pow(C_dash,d,N)
        print(" Resulting plaintext after decryption of C'(C'^d mod N):",C_decrypted,file=TeeFile(sys.__stdout__,f))

        plain=(C_decrypted*r_inverse)%N
        Label(newwin, text="plain text of block "+str(i//block_size)+" in decimal is:").grid(row=rows)
        k=Entry(newwin)
        k.grid(row=rows,column=1)
        rows+=1
        k.insert(0,str(plain))
        plain=hex(plain).split('x')[1]
        
        plain_block=''

        for p in range(0,len(plain),2):
            plain_block=plain_block+chr(int(plain[p:p+2],16))
            plaintext_f=plaintext_f+chr(int(plain[p:p+2],16))

        print("plaintext  got after attack : ",plain_block,file=TeeFile(sys.__stdout__,f))
       
    Label(newwin, text="Plain text got after choosen ciphertext attack").grid(row=rows)
    
    e4 = Entry(newwin)
    e4.grid(row=rows,column=1)
    
    e4.insert(0,str(plaintext_f))
    print("Plaintext got after choosen cipher text attack:",plaintext_f,file=TeeFile(sys.__stdout__,f))
    print("\n",file=TeeFile(sys.__stdout__,f))
if __name__ == "__main__":
    choosen_ciphertext_attack()
        

        

       # M=pow(M_actual_sign,e,N)


        
    
    

    


    

    

