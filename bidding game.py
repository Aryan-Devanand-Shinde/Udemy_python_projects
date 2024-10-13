print('''BIDDING GAME
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
bidders={}
flag='y'

while(flag=='y'):
    bidder=input("What's the name of bidder? ")
    bid=int(input("What the amount of bid? "))
    
    bidders[bidder]=bid

    anymore=input("Is any more any bidder? y or n \n")
    if anymore=='y':
        flag='y'
    else:
        flag='n'

max=0
for key in bidders:
    if max<bidders[key]:
        max=bidders[key]
        max_bidder=key

print(f"The max bid is{max} bidder is: {max_bidder}")

