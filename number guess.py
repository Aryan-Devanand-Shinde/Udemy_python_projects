import random
no_to_be_guessed_is=random.randint(1,100)
print(no_to_be_guessed_is)
print("WELCOME TO THE GAME OF GUESS:::")
lvl=int(input("1. EASY\n2. MEDIUM\n3. HARD\n"))

def easy():
    print("YOU have choosen the EASY mode")
    print("You will get 15 chances to guess a number")
    n=15
    return n

def medium():
    print("YOU have choosen the MEDIUM mode")
    print("You will get 10 chances to guess a number")
    n=10
    return n

def hard():
    print("YOU have choosen the HARD mode")    
    print("You will get 5 chances to guess a number")
    n=5
    return n

def guess_check(a,no_to_be_guessed_is):
    while(a>0):
        g=int(input("Guess the number: "))
        if g>no_to_be_guessed_is:
            print("the guessed no is to HIGH")
            print(f"{a-1} chances left")
        elif g<no_to_be_guessed_is:
            print("the guessed no is to LOW")
            print(f"{a-1} chances left")
        else:
            print("YOU WON THE GAME")
        a=a-1            

if lvl==1:
    a=easy()
    guess_check(a,no_to_be_guessed_is)
elif lvl==2:
    a=medium()
    guess_check(a,no_to_be_guessed_is)
elif lvl==3:
    a=hard()
    guess_check(a,no_to_be_guessed_is)
else:
    print("choose the valid no.")
