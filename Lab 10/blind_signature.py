from tkinter import *
p=0
q=0
plaintext=0
r=0
e=0
e4=0
e5=0
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
def bs():
    global newwin,p,q,r,e,plaintext,e4,e5
    newwin = Tk()
    display = Label(newwin, text="Blind Signature  attack")
    display.grid(row=1,column=1)

    newwin.title("Blind Signature attack")
    Label(newwin, text="Message is").grid(row=2)
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

    Button(newwin, text='Submit', command=blind_signature).grid(row=7)

    newwin.mainloop()

def blind_signature():
    rows=8
    global p,q,r,e,plaintext,e4,e5
    plaintext=plaintext.get()
    f=open("Program-7.output.txt","a")
    p=int(p.get())
    print("p:",p,file=f)
    q=int(q.get())
    print("q:",q,file=f)
    N=p*q
    print("N:",N)
    e=int(e.get())
    print("e:",e,file=f)
    phi=(p-1)*(q-1)
    d=modInverse(e,phi)
    #print("private key d is",d)
    if d==-1:
        Label(newwin,text="Signature").grid(row=rows)
        e4 = Entry(newwin)
        e4.grid(row=rows,column=1)
        e4.insert(0,"No private key d exists  ,exiting")
        print("No private key d present ,exiting")
        print("No private key d present ,exiting",file=f)
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
    r_inverse=modInverse(r,N)
    #print("r_inverse is ",r_inverse)
    count=1
    # while r_inverse==-1 and count!=3:
    #     r=int(input("enter the value of r\n"))
    #     r_inverse=modInverse(r,N)
    #     count=count+1

    if r_inverse==-1 :
        Label(newwin,text="Signature").grid(row=rows)
        e4 = Entry(newwin)
        e4.grid(row=rows,column=1)
        e4.insert(0,"No r inverse exists present ,exiting")
        print("exiting")
        return -1
    M=''
    Message=''
    Signature=''
    print("No.of blocks ",len(plaintext)/block_size)
    print("No.of blocks ",len(plaintext)/block_size,file=f)

    print("Blocksize in bits is ",block_size*8)
    print("Blocksize in bits is ",block_size*8,file=f)
    for i in range(0,len(plaintext),block_size):
        M=''
        for j in range(block_size):
            M=M+hex(ord(plaintext[i+j])).split('x')[1]
        print("\n------------------------------------\n")
        print("block ",i//block_size)
        print("block ",i//block_size,file=f)
        M_hex=M
        M=int(M,16)
        print("Message in decimal:",M)
        M_dash=(M*pow(r,e))%N
        print("Intermediate in decimal(Mr^e mod N)(M'):",M_dash)
        

        M_signature=pow(M_dash,d,N)
        print(" Intermediate in decimal(M^d mod N)(M''):",M_signature)

        M_actual_sign=(M_signature*r_inverse)%N
        #print("Blind signature in  ",M_actual_sign)
        Label(newwin, text="Blind Signature of block  "+str(i//block_size)+" in decimal is:").grid(row=rows)
        
        k=Entry(newwin)
        k.grid(row=rows,column=1)
        rows+=1
        k.insert(0,str(M_actual_sign))
        print("Signature in decimal ",M_actual_sign)
        M_actual_sign=hex(M_actual_sign).split('x')[1]
        if len(M_actual_sign)%2!=0:
            M_actual_sign='0'+M_actual_sign

        
        Sign_block=''
        for p in range(0,len(M_actual_sign),2):
            Sign_block=Sign_block+chr(int(M_actual_sign[p:p+2],16))
            Signature=Signature+chr(int(M_actual_sign[p:p+2],16))

        print("Blind signature  of block: ",Sign_block)
       

        #verifying at reciever side
        M_actual_sign=int(M_actual_sign,16)
        M_verify=pow(M_actual_sign,e,N)
        M_verify='{0:0{1}b}'.format(M_verify,block_size*8)
        Message_block=''
        for k in  range(0,len(M_verify),8):
            Message_block=Message_block+chr(int(M_verify[k:k+8],2))
            Message=Message + chr(int(M_verify[k:k+8],2))
        print("Reconstructed message:",Message_block)
        print("\n------------------------------------\n")
    Label(newwin, text="Blind Signature  is").grid(row=rows)
    e4 = Entry(newwin)
    e4.grid(row=rows,column=1)
    rows=+1
    
    #Label(newwin,text="Fully reconstructed message is").grid(row=rows)
    
    # e5=Entry(newwin)
    # e5.grid(row=rows,column=1)
    rows+=1
    e4.insert(0,str(Signature))
    e5.insert(0,str(Message))
    print("Blind Signature of text:",Signature)
    print("Fully Reconstructed message :",Message)
if __name__ == "__main__":
    blind_signature()
        

        

       # M=pow(M_actual_sign,e,N)


        
    
    

    


    

    

