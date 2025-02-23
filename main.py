def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents  

from stats import num_words, char_count, make_list, sort_dict
   
          
          
          
            

def main(): 
    text = get_book_text("./books/frankenstein.txt")
    length = num_words(text)
    count = char_count(text)
    #print(f"{length} words found in the document")
    list = make_list(count)
    #print(list)
    #print(count)
    sort_dict(list)
    #print(list)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for dict in list:
       for letter in dict:
        if letter.isalpha() == True:
            print(f"{letter}: {dict[letter]}")
    print("============= END ===============")

main()