print("WELCOME TO THE CALCULATOR")

def clear_():
    return 0

def addition_(ans,inn):
    return ans+inn

def substraction_(ans,inn):
    return ans-inn

def multiplication_(ans,inn):
    return ans*inn

def division_(ans,inn):
    if inn!=0:
        return ( ans/inn)

def modulas_(ans,inn):
    if inn!=0:
        return ans%inn

ans=0
a=0
b=0

print('''MENU
      1.ADDITION
      2.SUBSTRACTION
      3.MULTIPLICATION
      4.DIVISION
      5.MODULAS
      6.CLEAR''')
   
y_n='y'
while(y_n=='y'):
    a=int(input("Enter the 1st no: "))
    b=int(input("Enter the 2nd no: "))
    c=input("Enter the operator to operate on: ") 
    cal_operations={'+':addition_(a,b),'-':substraction_(a,b),'*':multiplication_(a,b),'clear':clear_(),'/':division_(a,b),'%':modulas_(a,b)}
    for x in cal_operations:
        if x==c:
            y=cal_operations[c]
    print(y)
    y_n=input("do u want to continue?:y or n").lower()  




 


