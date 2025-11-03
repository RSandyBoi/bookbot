def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
def char_sort(char_count):