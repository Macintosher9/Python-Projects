temp1=input("Would you like convert your temperature into celsius or fahrenheit?")
if temp1 == "celsius" or "Celsius":
    fahreheit1 = int(input("What tempeature would you like to convert to celsius?"))
    celsius1 = ((fahreheit1-32)*(5/9))
    print(fahreheit1,"degree in celsius is",celsius1,"degree fahrenheit")
elif temp1 == "fahrenheit" or "Fahrenheit":
    celsius2 = int(input("What temperature would you like to convert to fahrenheit?"))
    fahreheit2 = ((celsius2*5/9)+32)
    print(celsius2,"degree in fahreheit is", fahreheit2,"degree celsius")
