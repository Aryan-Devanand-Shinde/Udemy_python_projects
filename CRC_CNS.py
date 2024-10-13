# take divisor and divident input in binary

divisor = input("divisor: ")
divident = input("divident: ")


new_divident = int(divident)


len_of_divisor = len(divisor)

# added zeros accordingly divisor
for i in range(1,len_of_divisor):
    new_divident = new_divident*10

leng = len(str(new_divident))
print(leng)
# divide and use x-or in that
# check leave first of every time
# 00 or 11 is 0 
# 01 or 10 is 1 

l1 = []  # list of divisor
l2 = []  # list of dividents   
dummy=[]
remainder = []
quotient = []
zero=['0','0','0','0']

# def dumy(a,b):
#     dummy=[]
#     for i in range(a,b):
#         dummy.append(l2[i])
#     print(dummy)    

def compare(dzr,dnt):
    global dummy
    print(dzr)
    print(dnt)
    for i in range(0,4):
        if dzr[i]==dnt[i]:
            dummy[i]=0
        else:
            dummy[i]=1
    print(dummy)

for i in divisor:
    l1.append(i)

for i in str(new_divident):
    l2.append(i)

print(divisor)
print(divident)
print(new_divident)


for i in range(0,4):
    dummy.append(l2[i])

if dummy[0]==1:
    quotient.append(1)
    compare(dummy,zero)
else:
    quotient.append(0)
    compare(dummy,l1)        

































a=0
b=4
# c=leng-b+1
# print(c)
# while(c):
#     dumy(a,b)
#     print(a , b)    
#     # a=a+1
#     b=b+1
#     c=c-1

# compare first 4 of both

    
