def num_words(text):
    text_list = text.split()
    length = len(text_list)
    return length

def char_count(text):
    count = {}
    text = text.lower()
    text_list = text.split()
    for word in text_list:
        for character in word:
            if character in count:
                count[character] += 1
            else :
                count[character] = 1
    return count
def make_list(dict):
    list = []
    for pair in dict:
        list.append({pair:dict[pair]})
    return list

def sort_on(dict):
        for char in dict:
            return dict[char]

def sort_dict(dict):
    dict.sort(reverse=True, key=sort_on) 
    return dict
    