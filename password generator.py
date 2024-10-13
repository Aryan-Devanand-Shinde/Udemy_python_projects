# PASSWORD GENERATOR
import random
letters=list(('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))

numbers=list(('1','2','3','4','5','6','7','8','9','0'))

symbols=list(('!','`','@','#','%','$','^','&','*','(',')'))

print("Welcome to the PASSWORD GENERATOR!!")
let_no=int (input("How many letters do u want in your password: "))
numerals_no=int(input("How many numbers do u want in your password: "))
symbol_no=int(input("How many symbols do u want in your password: "))

# EASY PASSWORD
password=list(())
for i in range(0,let_no):
    random_no=letters[random.randint(0,len(letters)-1)]
    password.append(random_no)

for i in range(0,numerals_no):
    random_no=numbers[random.randint(0,len(numbers)-1)]
    password.append(random_no)

for i in range(0,symbol_no):
    random_no=symbols[random.randint(0,len(symbols)-1)]
    password.append(random_no)


random.shuffle(password)

# to make list into string
str=''
print (str.join(password))