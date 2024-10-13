# TIP CALUCULATOR
print("Welcome to the tip calculator")
bill=float(input("Put the amount of your bill: "))
tip=int(input("How much tip you want to give??10 ,12 ,15: "))
split=int(input("How many people to be contributed?? "))
bill_per_person=(bill+tip)/split
print(f"The amount that each person should pay: {bill_per_person}")