# trying this class thing on my own describing my girlfriend

class Girlfriend:
    def __init__(self, name, age, height, hair, personality):
        self.name= name
        self.age = age
        self.height = height
        self.hair = hair
        self.personality= personality
        self.sexy = 12

    def full_description (self):
        total_description = f"{self.name.title()} is {self.age}, is {self.personality} with {self.hair} hair, who is {self.age} and {self.height} feet tall."
        return total_description
    
    def sexiness (self):
        print(f"She is an {self.sexy} out of 10!")

my_girlfriend = Girlfriend ("Natalie", 24, "6'", "blonde", "wonderful and sarcastic")
print(my_girlfriend.full_description())
my_girlfriend.sexiness()
