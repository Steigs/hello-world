# page 174

from car_class import Car

my_new_car = Car("hummer", "h2", 2010)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 25
my_new_car.read_odometer()