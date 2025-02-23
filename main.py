import sys
def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents  

from stats import num_words, char_count, make_list, sort_dict          

def main(): 
    file_path = sys.argv[1]
    
    try:
        text = get_book_text(file_path)
        length = num_words(text)
        count = char_count(text)
    #print(f"{length} words found in the document")
        list = make_list(count)
    #print(list)
    #print(count)
        sort_dict(list)
    #print(list)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}")
        print("----------- Word Count ----------")
        print(f"Found {length} total words")
        print("--------- Character Count -------")
        for dict in list:
            for letter in dict:
                if letter.isalpha() == True:
                    print(f"{letter}: {dict[letter]}")
        print("============= END ===============")
    except Exception:
        print("please provide path to book")
        sys.exit(1)
main()