
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
  

def blind_signature():
    plaintext=input("Enter the plaintext\n")
    N=int(input("enter the N\n"))
    p=int(input("Enter the p\n"))
    q=int(input("Enter the q\n"))
    e=int(input("Enter the public key e\n" ))
    phi=(p-1)*(q-1)
    d=modInverse(e,phi)
    print("private key d is",d)
    if d==-1:
        print("No private key d present ,exiting")
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
    print("No.of blocks ",len(plaintext)/block_size)

    print("Blocksize in bits is ",block_size*8)
    r=int(input("Enter the value of r\n"))
    r_inverse=modInverse(r,N)
    print("r_inverse is ",r_inverse)
    count=1
    while r_inverse==-1 and count!=3:
        r=int(input("enter the value of r\n"))
        r_inverse=modInverse(r,N)
        count=count+1

    if r_inverse==-1 and count==3:
        print("exiting")
        return -1
    M=''
    Message=''
    for i in range(0,len(plaintext),block_size):
        M=''
        for j in range(block_size):
            M=M+hex(ord(plaintext[i+j])).split('x')[1]
        M_hex=M
        M=int(M,16)
        M_dash=M*pow(r,e)%N

        M_signature=pow(M_dash,d,N)

        M_actual_sign=(M_signature*r_inverse%N)
        print("block ",i//block_size,"signature is ",M_actual_sign)

        #verifying at reciever side

        M_verify=pow(M_actual_sign,e,N)
        M_verify='{0:0{1}b}'.format(M_verify,block_size*8)
        
        for k in  range(0,len(M_verify),8):
            Message=Message + chr(int(M_verify[k:k+8],2))
        
    print("Message at reciever is :",Message)
if __name__ == "__main__":
    blind_signature()
        

        

       # M=pow(M_actual_sign,e,N)


        
    
    

    


    

    

