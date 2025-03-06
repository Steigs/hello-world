# project on page 123

prompt = "\nLet me know what toppings you want on your pizza: "
prompt+= "\nSay 'quit' when you are done adding toppings."

toppings = True

while toppings:
    message = input(prompt)

    if message == 'quit':
        toppings = False

    else:
        print(f"You got it, lets get {message} added to your pizza!")



prompt = "\nGood evening, how old are you? "


while True:
    message = input(prompt)
    

    if message.isdigit():
        age = int(message)

        if age < 3:
            print("You get in for free!")
        elif age < 12:
            print("The cost of your ticket is $10.")
        elif age >= 12:
            print("The cost of your ticket is $15.")
    else:
        print("Invalid input. Exiting the program.")
        break
