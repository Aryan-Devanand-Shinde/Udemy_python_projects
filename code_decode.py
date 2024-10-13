alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("ENCODE or DECCODE: ").lower()
text=input("Enter your text: ")
shift=int(input("shift numbers: "))

str=''
enpt=[]
def encrypt(text,shift):
    for i in text:
        for j in range(0,len(alphabet)-1):
            if i==alphabet[j]:
                if shift+j<=25:
                    enpt.append(alphabet[shift+j])
                elif i==" ":
                    enpt.append("_")    
                else:
                    enpt.append(alphabet[shift+j-25])    

def decode(text,shift):
    for i in text:
        for j in range(0,len(alphabet)-1):
            if i==alphabet[j]:
                if shift-j>=0:
                    enpt.append(alphabet[shift-j])
                elif i==" ":
                    enpt.append("_") 
                else:
                    enpt.append(alphabet[shift-j+25])        

                
if direction=='encode':
    encrypt(text,shift)    
elif direction=='decode':
    decode(text,shift)   
else:
    print("wrong input")                 

print(str.join(enpt))