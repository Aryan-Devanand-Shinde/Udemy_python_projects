# HAMMING CODE
hamming = [' ',' ',' ','p4',' ',' ','p3',' ','p2','p1',' ']

print("the code should be in binary and 7 bits")
input_code = input("code to be send: ")

ip_code=[]
for i in input_code:
    ip_code.append(i)

print(input_code)

z=0

for i in range(0,len(hamming)):
    if hamming[i]==' ':
        hamming[i]=input_code[z]
        z=z+1
            
print(hamming)        