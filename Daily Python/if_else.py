average=.175
if average <.300:
    print("You are terrible.")
else: 
    print("Shit you got a chance!")

average=.310
if average <.220:
    print("You are terrible.")
elif average <.300:
    print("Well keep working and maybe you'll get there.")
else: 
    print("Shit, you got a chance!")

average = .350
if average <.220:
   result = "shitty"
elif average <.300:
    result = "decent"
else:
    result = "an all star"
print(f"This kid is gonna be {result}.")