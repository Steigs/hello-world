requested_toppings= ["pepperoni","green peppers","extra cheese"]
for requested_toppings in requested_toppings:
    print(f"Added {requested_toppings}.")
print("\nFinished making your pizza!")


requested_toppings= ["pepperoni","green peppers","extra cheese"]
for requested_toppings in requested_toppings:
    if requested_toppings =="green peppers":
        print("Sorry we are out of green peppers")
    else:
        print(f"Added {requested_toppings}.")
print("\nFinished making your pizza!")


requested_toppings= []

if requested_toppings:
    for requested_toppings in requested_toppings:
        print(f"Added {requested_toppings}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings= ["pepperoni","green peppers","extra cheese","olives"]
requested_toppings=["anchovies","pepperoni"]

for requested_toppings in requested_toppings:
    if requested_toppings in available_toppings:
        print(f"Added,{requested_toppings}")
    else:
        print(f"Sorry, we don't have {requested_toppings}.")
print("Your pizza is finished!")