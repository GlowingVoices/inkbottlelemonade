import sys
from yaml_functions import *
from datetime import datetime

def log(input):
    f = open("logs.txt","a")
    f.write(str(input) + "\n\n")
    f.close()

def reformat_date(date_str):
    # Convert the string to a datetime object
    datetime_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %z")

    # Reformat the date without time
    reformatted_date = datetime_obj.strftime("%a %b %d %Y")

    return reformatted_date

#given an input dictionary, clean it's subitems.
def recursive_clean(settler):
    string_contents = settler['Chapter']['content']

    #This is what we will edit -> this line becoems return & edit the content
    fm = return_jekyll_frontmatter(settler['Chapter']['content'])
    settler['Chapter']['content'] = remove_jekyll_frontmatter(settler['Chapter']['content'])

    #We're going to use this to update the post name from the file
    #and also to add in author info and date of edit/upload

    #if 'title' in fm:
    #    log(fm['title'])

    #log(settler['Chapter']['name'])

    if 'title' in fm:
        #log(fm['title'])
        settler['Chapter']['name'] = fm['title']


    addendum = ""
    if 'author' in fm:
        addendum += "\n" + "**author:** "  +fm['author']

    if 'date' in fm:
        addendum += "\n\n" + "**date:** " +reformat_date(fm['date'])

    hash_index = settler['Chapter']['content'].find("#")
    n_index = settler['Chapter']['content'].find("\n", hash_index)

    # Insert the addendum at the line break index
    settler['Chapter']['content'] = settler['Chapter']['content'][:n_index] + addendum + settler['Chapter']['content'][n_index:]
    log(settler['Chapter']['content'])


    #so if the yaml has a title, it'll use that title instead of the one defined in the initialization summary


    """
    if isinstance(settler,dict) and "sub_items" in settler['Chapter']:
        log(type(settler['Chapter']))
        log(settler['Chapter'])
        recursive_clean(settler['Chapter']['sub_items'])
        """

    if 'sub_items' in settler['Chapter'] and settler['Chapter']['sub_items']:
        for sub_item in settler['Chapter']['sub_items']:
            recursive_clean(sub_item)


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
            if 'Chapter' in every:
                recursive_clean(every)

                #subsections (e.g. Bang-bang of PID) load as part of the PID json set

            #log(chapter_dictionary)
            #log(type(chapter_dictionary))
            #the non-string is a separator

    #FINALLY
        #Okay, so the structure of the input it dictionary -> list -> dictionary
        #the first dictionary contains the 'sections';  the list
        #the list contains the set of dictionaries, each containing one piece of information

    sys.stdout.write(json.dumps(book))
