def intial_permutation(block):
    a=[[0 for i in range(8)] for i in range(8)]
    num=2
    
    for i in range(7,-1,-1): 
        for j in range(4): #first four rows
            a[j][i]=block[num-1]
            num=num+2
    num=1
    
    for i in range(7,-1,-1):
        for j in range(4,8): #last four rows
            a[j][i]=block[num-1]
            num=num+2
    #print(a)
    block=""
    str=""
    for i in range(8): 
        block=block+str.join(a[i]) #concatenation of rows
    return block

def final_permutation(block):
    a=[[0 for i in range(8)] for i in range(8)]
    num=0
    for i in range(1,8,2):       # odd alternative columns
        for j in range(7,-1,-1): 
            num=num+1
            a[j][i]=block[num-1]
    
    for i in range(0,8,2):     # even alternative columns
        for j in range(7,-1,-1):
            num=num+1
            a[j][i]=block[num-1]
    block=""
    str=""
    for i in range(8):
        block=block+str.join(a[i]) #concatenation of rows
    return block

def ascii_tobinary(plain_text):
    binary=''
    block=''
    for j in range(len(plain_text)):
        binary=bin(ord(plain_text[j]))
        block=block+'0'*(8-(len(binary)-2))+binary[2:]
    return block


def binaryto_ascii(block):
    text=''
    for j in range(0,64,8):
        text=text+chr(int(block[j:j+8],2))
    return text

def printf(block):
 	for i in range(8):
 		print(block[i*8:(i+1)*8],end='	')


if __name__ == '__main__':
    plain_text=input("enter the string\n")
    plain_text=plain_text.replace(' ','')
    #print(plain_text)
    if len(plain_text)%8!=0 :
    	plain_text=plain_text + ' '*(8-(len(plain_text)%8)) #making text blocks of 8 characters
    
    #print(binary,len(binary))
    block=''
    for j in range(0,len(plain_text),8): #multiple blocks

        block=ascii_tobinary(plain_text[j:j+8])
        print("+++++++++++BLOCK ",(j//8 +1),"++++++++++++")
        print("8 character block is :",plain_text[j:j+8],"\n 64 bit block is:")
        printf(block)
        block=intial_permutation(block)
        print("\nAfter Intial permutation of block is:")
        printf(block)
        #print("Ascii conversion of intial permuted block ",(j//64+1),"is:\n",binaryto_ascii(block))
        block=final_permutation(block)
        print("\nAfter Final permutation of block is:")
        printf(block)
        print("\nAscii conversion of final permuted block is:",binaryto_ascii(block))
        print("-------------------------------")

   

    
    