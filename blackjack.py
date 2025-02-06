# You get double the money if you win
username = input('What is your name?\n')
moneypot = int(input('How much money are you willing to bet?\n'))

import random
cardrandomizer = random.randint(1,10)+random.randint(1,10)
print('Your cards total are:',cardrandomizer)

def gameplay():
    global cardrandomizer
    global moneypot
    asking = input('Would you like to hit, stay\n')
    if asking=='hit':
        cardrandomizer2=cardrandomizer+random.randint(1,10)
        gameplay()
        if cardrandomizer2>21:
            print('You went over 21, you lost',moneypot)
        elif cardrandomizer2==21:
            print('You won',moneypot*2)
            quit()
    elif asking=='stay':
        quit()