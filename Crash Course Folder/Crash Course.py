# Here is what I learn from my new book call Python Crash course by Eric Matthes
firstname="mac"
lastname="chang"
fullname=f"{firstname} {lastname}"
print(f"Hello, {fullname.title()}!\n")

# The \n\t is to indent and add whitspace between each word
print("To do list:\n\tLaundry\n\tCleaning my room\n\tOthers")

pizzas = ['Meat Lover', 'Pepperoni', 'Sausage']
for pizza in pizzas:
    print("I like",pizza)
print('I really like',pizzas[0])
