message= input("Tell me somehting and I will repeat it back to you: ")
print(message)

greeting = input("Please enter your name: ")
print(f"\nHow are you doing today {greeting.title()}?")

prompt = ("We need to know your name in order to better serve you.")
prompt +=("\nWhat is your name?: ")
name = input(prompt)
print(f"\nHello {name}!")