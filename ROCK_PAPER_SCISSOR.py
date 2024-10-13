import random
print("Welcome to ROCK-PAPER-SCISSORS")

comp=['rock','paper','scissor']

user_choice=input("your choice rock/paper/scissor\n")
comp_choice=comp[random.randint(0,2)]

print(f"your choice: {user_choice} & computer choice: {comp_choice}")

if user_choice==comp_choice:
    print("You WON")
else:
    print("You LOSE")    