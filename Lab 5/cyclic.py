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
    cipher=input("Enter the ciphertext \n")
    N=int(input("Enter N\n"))
    e=int(input("Enter e\n"))
    plaintext=''
    for i in cipher:
        temp=ord(i)
        plain=None
        c=0
        while c==0 or temp!=ord(i):
            c=c+1
            plain=temp
            temp=exp_modulo(temp,e,N)
        print(c)
        plaintext=plaintext+chr(plain)
    
    print("plaintext is: ",plaintext)
    ciphertext=''
    for i in plaintext:
        temp=exp_modulo(ord(i),e,N)
        ciphertext+=chr(temp)
    print("encrypting the plain text obtained: ",ciphertext)
            
if __name__ == "__main__":
    main()
    