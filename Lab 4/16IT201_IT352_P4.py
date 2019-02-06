import sys
from P1 import intial_permutation,final_permutation,ascii_tobinary
from P2 import round_key_gen
from  P3 import _16_rounds,printf
f=open("Output-4.txt","w")
class TeeFile(object):
    def __init__(self,*files):
        self.files = files
    def write(self,txt):
        for fp in self.files:
            fp.write(txt)


def DES(block,round_keys):
    global f
    block=intial_permutation(block)
    print("After Intial:",end=' ',file=TeeFile(sys.__stdout__,f))
    printf(block,f)
    print("\n\n",file=TeeFile(sys.__stdout__,f))
    block=_16_rounds(block,round_keys,f)
    print("\n",file=TeeFile(sys.__stdout__,f))
    block=final_permutation(block)

    return block

def main():
    global f
    plain_text=input("enter the string\n")
    #plain_text=plain_text.replace(' ','')
    #print(plain_text)
    
    key=input("enter the key\n")


    if len(plain_text) >40  :
        print("plaintext length more than 40 bytes")
        return 
    
    elif len(key)!=8:
        print("key length is more or less  than 8 bytes")
        return

    if len(plain_text)%8!=0 :
    	plain_text=plain_text + ' '*(8-(len(plain_text)%8))


    key=ascii_tobinary(key)
    round_keys=round_key_gen(key)
    block=''
    for j in range(0,len(plain_text),8): #multiple blocks

        block=ascii_tobinary(plain_text[j:j+8])
        print("+++++++++++BLOCK ",(j//8 +1),"++++++++++++",file=TeeFile(sys.__stdout__,f))
        print("Plaintext is:",plain_text[j:j+8],"\nBinary is   :",end=' ',file=TeeFile(sys.__stdout__,f))
        printf(block,f)
        print("\n",file=TeeFile(sys.__stdout__,f))
        block=DES(block,round_keys)
        print("After Final :",end=' ',file=TeeFile(sys.__stdout__,f))
        printf(block,f)
        #print("\nAscii conversion of final permuted block is:",binaryto_ascii(block))
        print("\n-------------------------------",file=TeeFile(sys.__stdout__,f))
        
if __name__ == '__main__':
    main()