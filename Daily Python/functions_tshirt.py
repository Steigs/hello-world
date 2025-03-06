# functions project on page 136

def make_shirt(size, text):
    '''display size and text on shirt'''
    print(f"A new order for a {size} shirt with {text} written on the front, just came in.")

make_shirt ('L' , 'Bitcoin Rocks')
make_shirt (size="Large", text= "Bitcoin rocks")


def make_shirt(text, size="Large"):
    '''display size and text on shirt'''
    print(f"A new order for a {size} shirt with {text} written on the front, just came in.")

make_shirt ('I Love Python')


def make_shirt(size, text = 'Bitches'):
    '''display size and text on shirt'''
    print(f"A new order for a {size} shirt with {text} written on the front, just came in.")

make_shirt ('Medium')
make_shirt ("Large)")
make_shirt ('Small', text="Bitcoin")

