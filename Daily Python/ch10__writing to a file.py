# page 190

# single line
from pathlib import Path

path=Path('programing.txt')
path.write_text ("I love programming!")


# multiple lines (overules single line)
contents = "I love programming...\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path=Path('programing.txt')
path.write_text(contents)