import argparse
import sys


def read_file(filename):
    data = None
    try:
        with open(filename, "rb") as f:
            data = f.read()
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise e
    return data

def read_file_lines(filename):
    data = None
    try:
        with open(filename, "rb") as f:
            data = f.readlines()
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise e
    return data

def split_newlines(data):
    return " ".join(data.split("\n"))

def process_file_contents(file_contents):
    bytes_count = len(file_contents)
    file_contents = file_contents.decode("utf-8")
    file_contents = split_newlines(file_contents)
    char_count = len(file_contents)
    word_count = len(file_contents.split())

    return [bytes_count, word_count, char_count]

def main():
    if len(sys.argv) == 2:
        contents = read_file(sys.argv[1])
        line_count = len(read_file_lines(sys.argv[1]))
        bytes_count, word_count, char_count = process_file_contents(contents)
        print(line_count, word_count, bytes_count)
        return

    description="Print newline, word, and byte counts for each file"

    parser = argparse.ArgumentParser(prog="Python 'wc'", description=description)

    parser.add_argument('-c', '--bytes', action="store", required=False)
    parser.add_argument('-l', '--lines', action="store", required=False)
    parser.add_argument('-m', '--characters', action="store", required=False)
    parser.add_argument('-w', '--words', action="store", required=False)

    args = parser.parse_args()
    print(args)

    if args.lines:
        print(len(read_file_lines(args.lines)))

    if args.bytes or args.characters or args.words:
        tern_option = args.bytes if args.bytes else args.characters if args.characters else args.words
        contents = read_file(tern_option)
        bytes_count, word_count, char_count = process_file_contents(contents)

        if args.bytes:
            print(bytes_count)
        elif args.words:
            print(word_count)
        elif args.characters:
            print(char_count)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))
