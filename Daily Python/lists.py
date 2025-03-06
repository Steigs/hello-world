cat_names = ["Weenie", "Levy", "Mrs. Weenerson","Miss Weenerskin","Trouble", "Short Legs", "Girly Pop","Mrs. Leavenworth", "Beanie", "Lev Lev","Beenie Weenie", "Stinky Butt"]
print(cat_names[0].upper())
print(cat_names[-1].lower())

message = f"We love our {cat_names[-1]} so much it hurts!"
print(message)



baseball= ["trout","ohtani","judge","soto"]
baseball[1]="pujols"
print(baseball)

baseball= ["trout","ohtani","judge","soto","mantle"]
baseball.append("pujols")
print(baseball)


basketball=[]
basketball.append('kobe')
basketball.append('lebron')
basketball.append('jordan')
print(basketball)
basketball.insert(2,"curry")
print(basketball)
del basketball[0]
print(basketball)
baseball.remove("mantle")
print(baseball)


print()
print(baseball)
popped_baseball=baseball.pop()
print(baseball)
print(popped_baseball)

like=baseball.pop(2)
print(f"Natalie's favorite baseball player is {like.title()}!")

print(baseball)
too_expensive="soto"
baseball.remove(too_expensive)
print(baseball)
print(f"\n {too_expensive.title()} is not worth the price!")