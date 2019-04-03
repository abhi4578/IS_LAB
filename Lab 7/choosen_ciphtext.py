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
  

def choosen_ciphertext_attack():

    f=open("Program-7.output.txt","w")
    plaintext=input("Enter the plaintext\n")
    print("Plaintext is :",plaintext,file=f)
    p=int(input("Enter the p\n"))
    print("p:",p,file=f)
    q=int(input("Enter the q\n"))
    print("q:",q,file=f)
    N=p*q
    print("N:",N,file=TeeFile(sys.__stdout__,f))
    e=int(input("Enter the public key e\n" ))
    print("e:",e,file=f)
    phi=(p-1)*(q-1)
    d=modInverse(e,phi)
    
    if d==-1:
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
    
    r=int(input("Enter the value of r\n"))
    print("r:",r,file=f)
    print("private key d is",d,file=TeeFile(sys.__stdout__,f))
    r_inverse=modInverse(r,N)
    print("r_inverse is ",r_inverse,file=TeeFile(sys.__stdout__,f))
    count=1
    while r_inverse==-1 and count!=3:
        r=int(input("enter the value of r\n"))
        r_inverse=modInverse(r,N)
        count=count+1

    if r_inverse==-1 and count==3:
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
        
        C=pow(M,e,N)
        print("ciphertext in decimal:",C,file=TeeFile(sys.__stdout__,f))
<<<<<<< HEAD
        M_actual_sign=hex(C).split('x')[1]
        Sign_block=''
        for p in range(0,len(M_actual_sign),2):
            Sign_block=Sign_block+chr(int(M_actual_sign[p:p+2],16))
        print("cipher in acii ",Sign_block)
=======
        
>>>>>>> 01075b9a9d2704b30458e6ea8d428dd23907f393
        C_dash=(C*pow(r,e))%N

        print("Intermediate in decimal(Cr^e mod N)(C'):",C_dash,file=TeeFile(sys.__stdout__,f))
        

        C_decrypted=pow(C_dash,d,N)
        print(" Resulting plaintext after decryption of C'(C'^d mod N):",C_decrypted,file=TeeFile(sys.__stdout__,f))

        plain=(C_decrypted*r_inverse)%N
  
        plain=hex(plain).split('x')[1]
        plain_block=''
        for p in range(0,len(plain),2):
            plain_block=plain_block+chr(int(plain[p:p+2],16))
            plaintext_f=plaintext_f+chr(int(plain[p:p+2],16))

        print("plaintext  got after attack : ",plain_block,file=TeeFile(sys.__stdout__,f))
       


    print("Plaintext got after choosen cipher text attack:",plaintext_f,file=TeeFile(sys.__stdout__,f))
    print("\n",file=TeeFile(sys.__stdout__,f))
if __name__ == "__main__":
    choosen_ciphertext_attack()
        

        

       # M=pow(M_actual_sign,e,N)


        
    
    

    


    

    

