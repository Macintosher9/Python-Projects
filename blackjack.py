# You get double the money if you win
username = input('What is your name?\n')
moneypot = int(input('How much money are you willing to bet?\n'))

import random
cardrandomizer = random.randint(1,10)+random.randint(1,10)
print('Your cards total are:',cardrandomizer)

def dealerturn():
    global moneypot
    dealerhand = random.randint(1,10)+random.randint(1,10)
    while dealerhand<17:
        dhand2=dealerhand+random.randint(1,10)
        print("Dealer hand currently is",dhand2)
        if dhand2==21:
            print("Dealer won",moneypot)
            break
        elif dhand2>21:
            print(username,"won",moneypot*2)
            break
        elif dhand2>=17:
            print("Dealer won",moneypot)
            break

def gameplay():
    global cardrandomizer
    global moneypot
    while cardrandomizer<21:
        asking = input('Would you like to hit, stay?\n')
        if asking == 'stay':
            dealerturn()
            break
        elif asking == 'hit':
            card2 = cardrandomizer+random.randint()
            print(card2)

gameplay()