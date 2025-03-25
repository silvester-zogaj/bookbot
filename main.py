import sys
from stats import (get_words, get_characters, sort_characters)



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_character_report(sorted_list):
    for item in sorted_list:
        print(f"{item['letter']}: {item['count']}")

def main():
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = get_words(book_text)
    character_count = get_characters(book_text)
    ordered_list = sort_characters(character_count)
    
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_character_report(ordered_list)
    print("============= END ===============")
    

   
    

main()
