# page 197 with Anthem by Ayn Rand

from pathlib import Path

path = Path('anthem.txt')

try: 
    contents = path.read_text()
except FileNotFoundError:
    print(f"Sorry that file {path} does not exist!")
else: 
    # Count the approximate number of words in the file:
    words =contents.split()
    num_words=len(words)
    print(f"The file {path} has about {num_words} words.")