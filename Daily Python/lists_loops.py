# project on page 127

sandwich_orders =["pb&j","pastrami","warrior","pastrami","pepperjack","pastrami"]
finished_orders=[]

print("we apologize but we are out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    completed=sandwich_orders.pop()

    print(f"Orders in the works: {completed.title()}")
    finished_orders.append(completed)

print("\nThe following orders have been completed:")
for finished_order in finished_orders:
    print(finished_order.title())


responses ={}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one palce in the world, where would it be? ")

    responses[name]=response

    repeat = input("Would you like to let another person respond? (yes/no)? ")
    if repeat == "no":
        polling_active=False

print ("\n---POLL RESULTS---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")