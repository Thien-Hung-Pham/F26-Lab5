# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/23/2026
# Purpose: Write data to a file.
# Usage: ./lab5b.py

# TO DO 1: Paste the code provided in readme.md file.
f = open('fruits.txt', 'w')
f.write('1. Apples are crunchy.\n2. Oranges are sweet, sour and juicy.\n3. Strawberries are sweet.\n4. Which fruit do you like?') # Write the data to the file.
f.close()
print("file fruits.txt has been created")

# TO DO 3: Run the 'ls' command.
# TO DO 4: Print the contents of fruits.txt in a loop.
print("Reading the file fruits.txt...")
f = open('fruits.txt', 'r')


while True:
    line = f.readline()
    if not line:
        break
    print(line.strip())

f.close()