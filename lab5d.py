# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 10/23/2026
# Purpose: Process File data.
# Usage: ./lab5d.py

# TO DO 1: Copy the files pythonStatements.txt and machineCode.txt in folder.


# TO DO 2: Follow the instructions from the readme.me file to create the exact output.

py = open('pythonStatements.txt', 'r')
machine = open('machineCode.txt', 'r')

for line in py:
    machine_line = machine.readline()
    code = line.split('#')[0].strip() # Remove comments and whitespace from the Python statement.
    print(f"{code} {machine_line.strip()}")

py.close()
machine.close()
