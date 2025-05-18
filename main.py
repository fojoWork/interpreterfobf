import sys
import os
import time

def translate_bf_to_python(bf_code):
    """Translate Brainfuck code to executable Python code"""
    # Filter only valid BF commands
    bf_code = ''.join(c for c in bf_code if c in '><+-.,[]')

    python_code = [
        "tape = [0] * 30000",
        "ptr = 0",
        "def get_input():",
        "    try: return ord(sys.stdin.read(1))",
        "    except: return 0",
        "",
        "# Translated Brainfuck code:"
    ]

    indent_level = 0
    for char in bf_code:
        if char == '>':
            python_code.append(" " * indent_level + "ptr += 1")
            python_code.append(" " * indent_level + "if ptr >= len(tape): tape.append(0)")
        elif char == '<':
            python_code.append(" " * indent_level + "ptr = max(0, ptr - 1)")
        elif char == '+':
            python_code.append(" " * indent_level + "tape[ptr] = (tape[ptr] + 1) % 256")
        elif char == '-':
            python_code.append(" " * indent_level + "tape[ptr] = (tape[ptr] - 1) % 256")
        elif char == '.':
            python_code.append(" " * indent_level + "print(chr(tape[ptr]), end='', flush=True)")
        elif char == ',':
            python_code.append(" " * indent_level + "tape[ptr] = get_input()")
        elif char == '[':
            python_code.append(" " * indent_level + "while tape[ptr] != 0:")
            indent_level += 4
        elif char == ']':
            indent_level = max(0, indent_level - 4)

    return '\n'.join(python_code)

def execute_python(python_code):
    """Execute the translated Python code"""
    try:
        exec(python_code)
    except Exception as e:
        print(f"\nError during execution: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 interpreter.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    print(f"Processing: {filename}...")
    time.sleep(1)  # Just for dramatic effect

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)

    print("\nTranslating Brainfuck to Python...")
    python_code = translate_bf_to_python(content)
    time.sleep(1)

    print("\nExecuting translated code:")
    print("=" * 40)
    execute_python(python_code)
    print("\n" + "=" * 40)
    print("\nExecution complete.")
