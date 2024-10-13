# BLACK JACK
import random

comp=[]
plyr=[]
cards=[2,3,4,5,6,7,8,9,10,11,10,10,10]

def calculate(lst):
    result= sum(lst)
    if (11 in lst) and result>21:
        result=result-10
    return result

t=2
while(t!=0):
    comp.append(random.choice(cards))
    plyr.append(random.choice(cards))
    t=t-1

print(comp)
print(plyr)

q=calculate(comp)
w=calculate(plyr)

if w > 21:
    print("YOU LOSE")
elif q>21:
    print("YOU WIN")
elif w>q:
    print("YOU WON")
else:
    print("YOU LOSE")  