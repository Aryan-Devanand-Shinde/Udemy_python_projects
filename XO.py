# XO GAME

def location(p1,e_o):
    global line1,line2,line3
    if e_o=='odd':
        e_o='O'
    else:
        e_o='X'

    if p1[0]=='a':
        if p1[1]=='1':
            line1[0]=e_o
            return
        if p1[1]=='2':
            line1[1]=e_o
            return
        if p1[1]=='3':  
            line1[2]=e_o
            return

    if p1[0]=='b':
        if p1[1]=='1':
            line2[0]=e_o
            return
        if p1[1]=='2':
            line2[1]=e_o
            return
        if p1[1]=='3':
            line2[2]=e_o
            return

    if p1[0]=='c':
        if p1[1]=='1':
            line3[0]=e_o
            return
        if p1[1]=='2':
            line3[1]=e_o
            return
        if p1[1]=='3': 
            line3[2]=e_o
            return


line1 = ['_','','_']
line2 = ['','!','']
line3 = ['_','','_']
selected=[]

print('''player 1 is X
         player 2 is O
         chances are alternatively
        ''')

print('''locations are as follows:

         [a1 a2 a3]
         [b1 b2 b3]
         [c1 c2 c3]
      
        ''')

t=9
e_o='odd'
flag=0
while(t):
    p1=input("location: ").lower()
    
    if p1 in selected:
        print("already selected select another")
        t=t+1
        pass
        
    else:
        selected.append(p1)
        if t%2==0:
            e_o='odd'
        else:
            e_o='even'    

        location(p1,e_o)
        # if t!=1:
        if line1[0]==line2[0]==line3[0] or line1[1]==line2[1]==line3[1] or line1[2]==line2[2]==line3[2] or line1[0]==line1[1]==line1[2] or line2[0]==line2[1]==line2[2] or line3[0]==line3[1]==line3[2] or line1[0]==line2[1]==line3[2] or line1[2]==line2[1]==line3[0] :
            if(e_o=="even"):
                print("'X' player1 WON")
            else:
                print("'O' player2 WON")    
            print(" ")
            print(line1)
            print(line2)
            print(line3)
            flag=1
            break

        print(line1)
        print(line2)
        print(line3)
        print(" ")
        print("already selected positions")
        print(selected)
        print(" ")
    t=t-1

if flag!=1:
    print("TIE")
