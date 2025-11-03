from stats import get_num_words
from stats import get_char_count

def get_book_text(f):
    return f.read()

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    with open("books/frankenstein.txt") as f:
        text = get_book_text(f)
        word_count = get_num_words(text)
        char_count= get_char_count(text)
        
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    

main()