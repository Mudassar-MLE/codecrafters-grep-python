import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!

#  https://docs.python.org/3/library/stdtypes.html#string-methods
def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\\d":
        return any(c.isdigit() for c in input_line)
    elif pattern == "\\w":
        return any(c.isalnum() or c == "_" for c in input_line)
    elif pattern.startswith("[") and pattern.endswith("]"):
        char_group = pattern[1:-1]
        if char_group.startswith("^"):
            char_group = char_group[1:]
            return any((lambda char: char not in char_group)(char) for char in input_line)
        else:
            return any((lambda char: char in char_group)(char) for char in input_line)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
