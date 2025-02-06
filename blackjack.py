username = input('What is your name\n')
moneypot = int(input('How much money are you willing to bet\n'))

import random
cardrandomizer = random.randint(1,10)+random.randint(1,10)
print('Your cards total are:',cardrandomizer)
def gameplay():
    global cardrandomizer
    asking = input('Would you like to hit, stay, or fold\n')
    if asking=='hit':
        cardrandomizer2 = random.randint(1,10)+cardrandomizer
    elif asking=='stay':
        quit()