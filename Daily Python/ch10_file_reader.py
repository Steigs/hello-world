# page 184

from pathlib import Path

path= Path("pi_digits.txt")
contents = path.read_text()
contents = contents.rstrip()
print(contents)




from pathlib import Path

path= Path("pi_digits.txt")
contents = path.read_text()

lines=contents.splitlines()
for line in lines:
    print(line)



from pathlib import Path

path= Path("pi_digits.txt")
contents = path.read_text()

lines=contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))



from pathlib import Path

path= Path("pi_million_digits.txt")
contents = path.read_text()

lines=contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(f"{pi_string[:52]}...")
print(len(pi_string))



from pathlib import Path

path= Path("pi_million_digits.txt")
contents = path.read_text()

lines=contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear.")
