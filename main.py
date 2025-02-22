def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents  

from stats import num_words

from stats import char_count

def main(): 
    text = get_book_text("./books/frankenstein.txt")
    length = num_words(text)
    count = char_count(text)
    print(f"{length} words found in the document")
    #print(text)
    print(count)
main()