from pathlib import Path

path = Path("hitting_book.txt")
contents = path.read_text()

# Print the contents of the file
print(contents)

# Count the number of characters in the file
character_count = len(contents)
print(f"Number of characters in the file: {character_count}")

# Count the number of words in the file
word_count = len(contents.split())
print(f"Number of words in the file: {word_count}")
