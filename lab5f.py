# Add comments before you do anything else.
#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Catch ZeroDivisionError
# Usage: ./lab5f.py

# TO DO 1: Complete the given functions.

def safe_divide(a,b):
  # divide a by b
  # Add an exception block to raise the error if error occurs because of a zero denominator.
  # Except block should display the appropriate error messages
  try:
    return a / b
  except ZeroDivisionError:
    return "Error: Division by zero is not allowed."

def main():
  print(safe_divide(10,5))  # works
  print(safe_divide(10,0))  # exception : Zero Division Error

if __name__ == "__main__":
  main()