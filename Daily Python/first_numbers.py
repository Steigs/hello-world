for value in range(1,11):
    print(value)

numbers=list(range(1,11))
print(numbers)

even_numbers=list(range(2,21,2))
print(even_numbers)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)

print(squares)

squares=[]
for value in range(1,11):
    squares.append(value**2)

print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)