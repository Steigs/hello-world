class Cat:
    '''A simple attempt to medel Lev Lev'''

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name=name
        self.age=age

    def sit(self):
        '''Simulate Lev sitting for a Greenie'''
        print(f"{self.name} always sits when she wants a Greenie")

    def loaf(self):
        '''Simulate Lev loafing'''
        print(f"{self.name} makes the perfect little bread loaf on her mat.")

my_cat=Cat ('Weanie Beanie', 2)
your_cat=Cat("Kink", 13)
print(f"My cat's name is {my_cat.name}")
print(f"Your cat's name is {your_cat.name}.")
print(f"My cat is {my_cat.age} years old.")
print(f"Your cat is {your_cat.age} years old.")
my_cat.sit()
my_cat.loaf()
your_cat.loaf()