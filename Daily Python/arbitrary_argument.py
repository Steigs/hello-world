#project on page 149

def sandwich_toppings(*toppings):
    """display topping being put on a sandwich"""
    print(f"\nMaking a Sandwich with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")

sandwich_toppings("turkey", "provalone")
sandwich_toppings("chicken", "bacon","Ranch")
sandwich_toppings ('P',"B","&J")


def build_profile (first, last, **user_info):
    '''Build a dictionary containing everything we know about a user.'''
    user_info["first_name"]=first
    user_info["last_name"]=last
    return user_info
user_profile = build_profile("Brady", "Steiger",
                             Girlfriend= "Natalie",
                             Cat= "Weenie",
                             Job="Baseball")
print(user_profile)



def make_car(manufacturer, model, **other_info):
    '''Build a dictionary containing everything we know about a car.'''
    other_info["make"]=manufacturer
    other_info["type"]=model
    return other_info
car = make_car("Porsche", "911",
                             Color= "Matte Gray",
                             Horsepower= "Alot",
                             Shininess="Very")
print(car)