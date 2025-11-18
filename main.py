import sys
if len(sys.argv)==1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_count_words, get_char_dict, sorted_dict
def get_book_text(file_path):
    with open(file_path) as f:
        # do something with f (the file) here
        file_contents = f.read()
    return file_contents

def main():
    contents=get_book_text(sys.argv[1])
    #print(contents)
    total_words = get_count_words (contents)
   
    dict_of_char=get_char_dict(contents)
    #print(dict_of_char)
    print_list=sorted_dict(dict_of_char)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print (f"Found {total_words} total words")
    print("--------- Character Count -------")
    for p in print_list:
        character=p["char"]
        number=p["num"]
        print(f"{character}: {number}")
   
main ()

