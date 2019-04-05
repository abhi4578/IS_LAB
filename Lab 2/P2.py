def permutation_choice1(block):
    a=[0 for i in range(56)]
    num=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    
    for i in range(len(num)):
            a[i]=block[num[i]-1]
    return a

def permutation_choice2(block):
    a=[0 for i in range(48)]
    num=[14,17,11,24,1,5,3,28,
        15,6,21,10,23,19,12,4,
        26,8,16,7,27,20,13,2,
        41,52,31,37,47,55,30,40,
        51,45,33,48,44,49,39,56,
        34,53,46,42,50,36,29,32]
    for i in range(len(num)):       
        a[i]=block[num[i]-1]
    return a

def ascii_tobinary(plain_text):
    binary=''
    block=''
    for j in range(len(plain_text)):
        block=block+ '{0:08b}'.format(ord(plain_text[j]))
    return block

def printf(block,f):
 	for i in range(8):
         print(block[i*8:(i+1)*8],end='  ',file=f)
         print(block[i*8:(i+1)*8], end='  ')

def round_key_gen(block):
    block=permutation_choice1(block)
    
    left_block=block[:28]
    right_block=block[28:]
    round_key=''
    round_keys=[]
        
    for i in range(1,17): 
        left_block.append(left_block.pop(0))
        right_block.append(right_block.pop(0))
        if i!=1 and i!=2 and i!=9 and i!=16:
            left_block.append(left_block.pop(0))
            right_block.append(right_block.pop(0))
        round_key=round_key.join(permutation_choice2(left_block+right_block))

            #print("\nRound",i,":",end=' ',file=f)
            ##print(round_key,file=f)
            #print("\nRound", i,":",end=' ')
            #printf(round_key,f)
        round_keys.append(round_key)
        round_key=''
    return round_keys

if __name__ == '__main__':    
    plain_text = input("enter string of atleast size of 8 characters\n")
    f = open("Round-Key.txt", "a")
    print("plaintext is:",plain_text,file=f)
    plain_text = plain_text.replace(' ', '')
    #making text blocks of 8 characters
    block=''
    i=1
    if len(plain_text) >=8:
        if len(plain_text) >8:
            i=int(input("Enter choice 1 or choice 2\n"))
            print("choice:",i,file=f)
        if i ==1 :
            block=ascii_tobinary(plain_text[:8])
        else :
             block=ascii_tobinary(plain_text[len(plain_text)-8:])
        ##print("64 bit block is :",block)
        round_key_gen(block)
        print()
        print("\n",file=f)
        f.close()
    else:
        print("enter string of atleast size of 8 characters")
   

    
    
