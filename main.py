def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def num_words(text):
    text_list = text.split()
    length = len(text_list)
    return length

    

def main(): 
    text = get_book_text("./books/frankenstein.txt")
    length = num_words(text)
    print(f"{length} words found in the document")
    #print(text)

main()