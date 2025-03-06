number=input("Enter a number and I'll tell you if it is odd or even: ")
number =int(number)

if number % 2 == 0:
    print(f"{number} is an even number!")
else: 
    print(f"\n{number} is an odd number!")