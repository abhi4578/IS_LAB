def exp_modulo(a,b,N):
    result=1
    while b>0 :
        a=a%N
        if b%2==1 :
            result=result*a%N
        a=a*a
        b=b//2
    return result%N

def main():
    #
    f=open("Program5-Output-CyclicProgram5.txt",'w')
    ciphertext=int(input("Enter the ciphertext \n"))
    N=int(input("Enter N\n"))
    e=int(input("Enter public key e\n"))
    print("Ciphertext:",ciphertext,"N:",N,"public key e:",e,"\n",file=f)
    plaintext=0
    temp=ciphertext
    c=0
    while c==0 or temp!=ciphertext:
        c=c+1
        plaintext=temp
        
        temp=exp_modulo(temp,e,N)
        #print("cyclic No:",c,"intermediate cipher:",temp)
        print("cyclic No:",c,"intermediate cipher:",temp,file=f)
        #print(c)
    
    
    print("plaintext is: ",plaintext)
    print("plaintext is: ",plaintext,file=f)
    ciphertext=exp_modulo(plaintext,e,N)
    print("encrypting the plain text obtained: ",ciphertext)
    print("encrypting the plain text obtained: ",ciphertext,file=f)
            
if __name__ == "__main__":
    main()
    
