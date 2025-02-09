# You get double the money if you win
username = input('What is your name?\n')
moneypot = int(input('How much money are you willing to bet?\n'))

import random
cardrandomizer = random.randint(1,10)+random.randint(1,10)
print('Your cards total are:',cardrandomizer)

def dealerturn():
    dealerhand = random.randint(1,10)+random.randint(1,10)
    while dealerhand<17:
        dhand2=dealerhand+random.randint(1,10)
        print("Dealer hand currently is",dhand2)
    if dealerhand >=17:
        print("Dealer won",moneypot)
    elif dealerhand>21:
        print(username,"Won",moneypot)

def gameplay():
    global cardrandomizer
    global moneypot
    asking = input('Would you like to hit, stay?\n')
    if asking=='hit':
        cardrandomizer2=cardrandomizer+random.randint(1,10)
        print(cardrandomizer2)
        gameplay()
        if cardrandomizer2>21:
            print('You went over 21, you lost',moneypot)
        elif cardrandomizer2==21:
            print('You won',moneypot*2)
    elif asking=='stay':
        dealerturn()

gameplay()