#Alien Color project on page 84

alien_color = "green"
if alien_color == "green":
    print("You earned 5 points!")

print()

alien_color="blue"
if alien_color =="green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

print()

alien_color="red"
if alien_color =="green":
    print("You earned 5 points!")
elif alien_color=="yellow":
    print("You earned 10 points!")
elif alien_color=="red":
    print("You earned 15 points!")

print()

#Stages of life if-elif-else

age=1
if age <2:
    person = "baby"
elif age <4:
    person="toddler"
elif age <13:
    person = "kid"
elif age <20:
    person="teenager"
elif age <65:
    person="adult"
else:
    person="elder"
print(f"You are officially a(n) {person}.")


print()

# favorite fruit page 85

favorite_fruits = ["banana", "strawberry","kiwi"]
favorite_fruits.append("lemon")==favorite_fruits
if "banana" in favorite_fruits:
    print("You really like bananas")
if "lemon" in favorite_fruits:
    print("You are a lemon lover.")
if "strawberry" in favorite_fruits:
    print("You must love a strawberry.")
if "waterwmelon" in favorite_fruits:
    print("Watermelon is pretty good.")
if "kiwi" in favorite_fruits:
    print("Kiwi is delicious.")