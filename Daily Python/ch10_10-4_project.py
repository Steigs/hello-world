# project 10-4 on page 192


from pathlib import Path


path=Path("guest.txt")

guest = input("Can I please have your name: ")
path.write_text(guest)




#project 10-5
from pathlib import Path

path = Path('guests.txt')

prompt = "\nHi, what's your name? "
prompt += "\nEnter 'quit' if you're the last guest. "

guest_names = []
while True:
    name = input(prompt)
    if name == 'quit':
        break

    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)