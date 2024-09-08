'''
1 for Rock
0 for Paper
-1 for Scissors
'''
import random
computer=random.choice([1,0,-1])
youstr=input("Enter your choice: ")

youdict={'r':1, 'p':0, 's':-1}
you=youdict[youstr]

reversedict={1:'Rock', 0:'Paper', -1:'Scissor'}

print(f'You chose {reversedict[you]} and computer chose {reversedict[computer]}')


# 1st example of code:

if(you==computer):
    print("Draw!")
else:
    if(computer==1 and you==0):
        print('You Win')
    elif(computer==1 and you==-1):
        print('You Lose')
    elif(computer==-1 and you==0):
        print('You Lose')
    elif(computer==-1 and you==1):
        print('You Win')
    elif(computer==0 and you==1):
        print('You Lose')
    elif(computer==0 and you==-1):
        print('You Win')


# or

# 2nd example of code:

if((computer-you)==-1 or (computer-you)==2):
    print('You Lose')
else:
    print('You Win')

# The basis of this code is (computer-you)