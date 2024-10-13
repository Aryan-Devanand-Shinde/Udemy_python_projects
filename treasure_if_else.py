print('''Welcome to Treasure Island.
Your mission is to find the treasure''' )

choice1=input("Left or Right?")
if choice1== 'right':
    print("Game Over")
else:
    choice2=input("Which color?")
    if choice2== 'yellow':
        print("You WON")
    else:
        print("Game Over")        