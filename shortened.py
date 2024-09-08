import random
computer=random.choice([1,0,-1])
youstr=input("Enter your choice: ")

youdict={'r':1, 'p':0, 's':-1}
you=youdict[youstr]

reversedict={1:'Rock', 0:'Paper', -1:'Scissor'}

print(f'You chose {reversedict[you]} and computer chose {reversedict[computer]}')

if((computer-you)==-1 or (computer-you)==2):
    print('You Lose')
else:
    print('You Win')

