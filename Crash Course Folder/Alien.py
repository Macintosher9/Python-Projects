def alienpoints():
    alien_0 = {'color': 'green'
            ,'speed':'slow'
            }
    print(alien_0['color'])
    if alien_0['color']=='green':
        print('You earned 5 points')
    elif alien_0['color']=='yellow':
        print('You earned 10 points')
    else:
        print('You earn 15 points')

def multiplealien():
    alien_0={'color':'green','points':5}
    alien_1={'color':'yellow','points':10}
    alien_2={'color':'red','points':15}
    aliens=[alien_0,alien_1,alien_2]
    for alien in aliens:
        print(alien)

multiplealien()