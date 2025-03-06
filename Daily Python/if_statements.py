cars=["audi","bmw","ferrari","honda"]
for car in cars:
    if car =="bmw":
        print(car.upper())
    else:
        print(car.title())

pizza_toppings= "pepperoni"
if pizza_toppings!="anchovies":
    print("Hold the anchovies!")

answer = 4
if answer!= 7:
    print("That is incorrect, please try again.")


    banned_users= ["john","ben", "matt"]
    user = "steven"
    if user not in banned_users:
        print(f"{user.title()}, let's hear your thoughts.")


car='subaru'
print("Is car=='subaru'? I predict True.")

print(car=='subaru')
print("\nIs car =='audi'? I predict False.")
print (car=='audi')