# Project on page 117

car=input("What kind of car of you looking to rent today: ")
print(f"\nLet's see if we can find you a {car.title()} today.")


print()
print("Welcome to Stack House!")
party = input("How many are in your party tonight? ")
party = int(party)

if party >=8:
    print(f"\nA table of {party} will be about a 25 minute wait.")
else: 
    print(f"\nFor {party}, right this way please.")

number = input("\nGive me any number you can think of and I will tell you if it is divisible by 6: ")
number = int(number)

if number % 6 == 0:
    print(f"\nWell of course {number} is divisible by 6.")
    print(number/6)
else: 
    print(f"\nNo chance that is divisible by 6.")
    print(number/6)