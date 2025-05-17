from main import filename  # Assuming filename is defined in main.py

def translate_bf_to_python(bf_code):
    """Translate Brainfuck code to Python"""
    py_code = [
        "tape = [0] * 30000",
        "ptr = 0",
        "def get_input():",
        "    return ord(sys.stdin.read(1)) if not sys.stdin.isatty() else 0"
    ]

    for char in bf_code:
        if char == '>':
            py_code.append("ptr += 1")
            py_code.append("if ptr >= len(tape): tape.append(0)")
        elif char == '<':
            py_code.append("ptr = max(0, ptr - 1)")
        elif char == '+':
            py_code.append("tape[ptr] = (tape[ptr] + 1) % 256")
        elif char == '-':
            py_code.append("tape[ptr] = (tape[ptr] - 1) % 256")
        elif char == '.':
            py_code.append("print(chr(tape[ptr]), end='')")
        elif char == ',':
            py_code.append("tape[ptr] = get_input()")
        elif char == '[':
            py_code.append("while tape[ptr] != 0:")
        elif char == ']':
            py_code.append("")  # Just for indentation end

    return '\n'.join(py_code)

def commands():
    """Read Brainfuck file and translate to Python"""
    try:
        with open(filename, 'r') as file:
            bf_code = file.read()

            # Filter only valid BF commands
            bf_code = ''.join(c for c in bf_code if c in '><+-.,[]')

            python_code = translate_bf_to_python(bf_code)

            # Write translated Python to new file
            output_filename = filename.replace('.bf', '.py') if filename.endswith('.bf') else filename + '.py'
            with open(output_filename, 'w') as out_file:
                out_file.write("import sys\n")
                out_file.write(python_code)

            print(f"Successfully translated to {output_filename}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    commands()
