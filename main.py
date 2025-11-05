from stats import get_num_words, make_list_of_char_dicts, sort_on
from stats import get_char_count
import sys

def get_book_text(f):
    return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    with open(f"{sys.argv[1]}") as f:
        text = get_book_text(f)
        word_count = get_num_words(text)
        char_count= get_char_count(text)
        
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    list_of_chars=make_list_of_char_dicts(char_count)
    list_of_chars.sort(key=sort_on, reverse=True)
    ##print(list_of_chars[2]["char"]) --> example frame of how to access the dict within the char list
    for i in list_of_chars:
        print(f"{i['char']}: {i['num']}")
        
main()