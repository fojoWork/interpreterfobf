import sys
import os

#read brainfuck file
if(len(sys.argv) < 2):
    print("Usage: python3 interpreter.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
print(f"Processing: {filename}...")

try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: {filename} not found")
    sys.exit(1)

#translate it into python code

#output it in the terminal
