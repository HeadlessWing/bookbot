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
        