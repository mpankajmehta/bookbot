def get_count_words(contents):
    num_words= len(contents.split())
    return num_words

def get_char_dict(contents):   
    char_dict={}
    #contents=contents.lower()
    for char in contents:
        lowered=char.lower()
        if lowered in char_dict:
            char_dict[lowered]+=1
        else:
            char_dict[lowered]=1
    #print(char_dict)
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_dict(dict_char):
    list_of_dict=[]
    for c in dict_char:
        empty={}
        if c.isalpha() ==True:
            empty["char"]=c
            empty["num"]=dict_char[c]
            list_of_dict.append(empty)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

