import sys
from yaml_functions import *

def log(input):
    f = open("logs.txt","a")
    f.write(str(input) + "\n")
    f.close()

if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports":
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    context, book = json.load(sys.stdin)
    json_pre_book = book
    open('logs.txt', 'w').close()

    """
    f = open("yay2.txt","w")
    g = open("yay.txt","w")
    l = open("omg.txt","w")

    f.write(str(json_pre_book))
    g.write(str(json_str_book))
    f.close()
    g.close()
    """
    #log(str(type(json_pre_book)))
    #log(str(len(json_pre_book)))
    book_list = list(json_pre_book.keys())
    book_sections = json_pre_book['sections'] #list

    """
    book_list_first = book_list[0] #the dictionary
    book_list_second = book_list[1] #this is just something called '__non_exhaustive'

    log(book_list)
    """
    #log(book_sections)
    #log(type(json_pre_book['sec

    for every in book['sections']:
        #if(str(type(every))=="<class 'dict'>"): #inside the third dictionary now
        if isinstance(every, dict): #pythonic way to check the type
            chapter_dictionary = every
            if 'Chapter' in chapter_dictionary:
                string_contents = chapter_dictionary['Chapter']['content']
                log(return_jekyll_frontmatter(string_contents))
                every['Chapter']['content'] = remove_jekyll_frontmatter(string_contents)


            #log(chapter_dictionary)
            #log(type(chapter_dictionary))
            #the non-string is a separator


    #FINALLY
        #Okay, so the structure of the input it dictionary -> list -> dictionary
        #the first dictionary contains the 'sections';  the list
        #the list contains the set of dictionaries, each containing one piece of information

    sys.stdout.write(json.dumps(book))
