prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your name?"

# By adding += to the same variable you can add to the message
name = input(prompt)
greeterchoice = """To even more personlize the message you see there are 6
greeter messages, type from 1 to 6."""
greeterchoice += "\n1. Hello,"
greeterchoice += "\n2. How is your day"
greeterchoice += "\n3. Greetings,"
greeterchoice += "\n4. Good morning"
greeterchoice += "\n5. Good afternoon"
greeterchoice += "\n6. Evening"
greeterchoice += "\nEnter number here:"

greetings = input(greeterchoice)
if greetings == "1":
    print("Hello",name)
elif greetings == "2":
    print("How is your day",name+"?")
elif greetings == "3":
    print("Greetings",name)
elif greetings == "4":
    print("Good morning",name)
elif greetings == "5":
    print("Good afternoon",name)
elif greetings == "6":
    print("Evening",name)