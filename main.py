import sys
from stats import *

usage_help = "Usage: python3 main.py <path_to_book>"

def get_book_text(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception as e:
        print(e)
        return None

def main():

    if len(sys.argv) != 2:
        print(usage_help)
        sys.exit(1)

    book = sys.argv[1]

    print("============ BOOKBOT ============")

    book_string = get_book_text(book)

    if not book_string:
        print(f'{book} not found')
        sys.exit(1)

    print(f"Analyzing book found at {book}...")

    words = get_num_words(book_string)

    print("----------- Word Count ----------")
    print(f'Found {words} total words')

    print("----------- Character Count ----------")
    counts = count_characters(book_string)
    pretty_print_character_counts(counts)

main()
