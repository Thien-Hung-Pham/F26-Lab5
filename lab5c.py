# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/23/2023
# Purpose: Process File data.
# Usage: ./lab5c.py

# TO DO 1: Run the code provided in readme.md file.
with open("rhyme.txt", "w") as dataFile :
  dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")

# TO DO 2: Open rhyme.txt file.
f = open('rhyme.txt', 'r')

# TO DO 3: Print the output as directed in readme.md file.

while True:
    line = f.readline()
    if not line:
        break
    word_len = len(line.split())
    print(f"{line.strip()} --- {word_len} words")
f.close()