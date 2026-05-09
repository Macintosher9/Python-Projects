import random
Places = ['THE GREAT WALL OF CHINA',
        'STATUE OF LIBERTY',
        'A TROPICAL ISLAND PARADISE',
        'GRAND CENTRAL TERMINAL',
        'THE GOLDEN GATE BRIDGE']
FilmQuotes = ['MAY THE FORCE BE WITH YOU',
            'THERE IS NO PLACE LIKE HOME',
            "I'LL BE BACK",
            'HERE IS LOOKING AT YOU KID',
            'TO INFINITY AND BEYOND']
PeopleTitles = ['FORMER PRESIDENT BARACK OBAMA',
                'CHAMPION ATHLETE SERENA WILLIAMS',
                'HOLLYWOOD STAR TOM HANKS',
                'SINGER AND SONGWRITER TAYLOR SWIFT', 
                'THE DYNAMIC DUO']
Foods = ['HOMESTYLE CHICKEN NOODLE SOUP',
        'FRESHLY BAKED APPLE PIE',
        'ICED COFFEE WITH OAT MILK',
        'SPAGHETTI AND MEATBALLS',
        'GRILLED CHEESE SANDWICH']
Phrases = ['BITE THE BULLET',
        'PIECE OF CAKE',
        'SEE YOU LATER ALLIGATOR',
        'A SIGHT FOR SORE EYES',
        'BETTER LATE THAN NEVER']

emptyLetters = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "__________________________")
inputed = input('Wheel Of Fortune Game\nAll guess have to be uppercased and only one letter is allowed\nType "Start" to start: ')
if inputed == "Start" or inputed =="start":
    Random = random.randint(1,5)
    if Random == 1:
        sentence = random.choice(Places)
        guessSentence = sentence
        empty = guessSentence.translate(emptyLetters)
        print("Category: Places")
        print("Sentence:", empty)
    elif Random == 2:
        sentence = random.choice(FilmQuotes)
        guessSentence = sentence
        empty = guessSentence.translate(emptyLetters)
        print("Category: Film Quotes")
        print("Sentence:", empty)
    elif Random == 3:
        sentence = random.choice(PeopleTitles)
        guessSentence = sentence
        empty = guessSentence.translate(emptyLetters)
        print("Category: People Titles")
        print("Sentence:", empty)
    elif Random == 4:
        sentence = random.choice(Foods)
        guessSentence = sentence
        empty = guessSentence.translate(emptyLetters)
        print("Category: Foods")
        print("Sentence:", empty)
    elif Random == 5:
        sentence = random.choice(Phrases)
        guessSentence = sentence
        empty = guessSentence.translate(emptyLetters)
        print("Category: Phrases")
        print("Sentence:", empty)

for letters in guessSentence:
    userGuess = input("Guess a letter: ")
    if userGuess.isalpha() == False:
        print("This is not a Letter, Enter a Letter")
    if userGuess == "End" or userGuess == "end":
        print("Game Ended")
        break
    else:
        if userGuess in guessSentence:
            print("You Got It!")
            guessSentence = guessSentence.index()
        else:
            print("Wrong Guess, Try Again")