# HANGMAN
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    ''')
import random
word_list=list(("ardvark","baboon","camel",'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow','dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox'))
# choosen_word=word_list[random.randint(0,len(word_list)-1)] instead of this we can use
choosen_word=random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
blank_list=[]
guess_list=[]

# print(choosen_word)

for i in range(0,len(choosen_word)):
    blank_list.append("_")

flag=True
life=len(stages)
while (flag and life>0) :
    letter_guess=input("word guess:").lower()
    if letter_guess not in guess_list:
        guess_list.append(letter_guess)

    if letter_guess  in guess_list:
        print(f"You  have already guessed this letter: {letter_guess}")

    for i in range (0,len(choosen_word)):
        if choosen_word[i]==letter_guess:
            blank_list[i]=choosen_word[i]
    print(blank_list)        
    if letter_guess not in choosen_word:
        print(stages[life-1])
        life-=1

    if life==0:
        flag=False
        print("YOU LOST ")

    if "_" not in blank_list:
        flag=False
        print("YOU WON") 




        


