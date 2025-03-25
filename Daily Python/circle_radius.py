def calculate_area(radius):
    area = 3.14 * radius * radius
    return area

radius_input = input("Enter the radius of the circle: ")
circle_area = calculate_area(radius_input)
print("The area of the circle is: " + circle_area)

if circle_area > 50:
    print("That's a large circle!")
else:
    print("That's a small circle!")
