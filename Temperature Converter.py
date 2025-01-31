askuser1=input("Would you like you temperature convert to Celsius or Fahreheit? ")

if askuser1=="fahreheit":
    C=int(input("What would you like to convert to fahreheit?\n"))
    F=((C*9/5)+32)
    print(C,"Celsius is",F,"Fahrehiet")

elif askuser1=="celsius":
    F=int(input("What would you like to convert to celsius?\n"))
    C=int((F-32)*5/9)
    print(F,"Fahreheit is",C,"Celsius")