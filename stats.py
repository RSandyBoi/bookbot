def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def make_list_of_char_dicts(dicts):
    list_of_dicts=[]
    for key in dicts:
        list_of_dicts.append({"char": key, "num": dicts[key]})
    return list_of_dicts

def sort_on(dict_list):
    return dict_list["num"]

    