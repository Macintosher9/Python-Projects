def city_country(city, country):
    cityName = f"{city}, {country}"
    return cityName.title()

while True:
    print("\nPlease tell me a city and country:")
    print("(enter 'quit' to exit)")

    city=input("City: ")
    if city == 'quit':
        break

    country=input("Country: ")
    if country == 'quit':
        break

    print(city_country(city, country))