print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")
print()
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language='Python          '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)
favorite_language=favorite_language.rstrip()
print(favorite_language)

favorite_language=favorite_language.lstrip()
favorite_language=favorite_language.strip()
print(favorite_language)

nostarch_url = "https://nostarch.com"
simple_url=nostarch_url.removeprefix("https://")
print(simple_url)

file_name= "python_notes.txt"
simple_name= file_name.removesuffix(".txt")
print(simple_name)
