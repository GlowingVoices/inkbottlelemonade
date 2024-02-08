import json
import sys
import re

def remove_frontmatter(content):
    # Pattern to find the frontmatter: starts with "---", followed by any characters (non-greedy), and ends with "---"
    pattern = r"^---.*?---\s*"
    # Replace the frontmatter with an empty string
    cleaned_content = re.sub(pattern, "# hi", content, flags=re.DOTALL)
    return "no"

def remove_jekyll_frontmatter(text):
    # Pattern to match the Jekyll front matter
    pattern = r'^---\s*\n.*?\n---\s*\n'

    # Use re.sub() to replace the front matter with an empty string
    cleaned_text = re.sub(pattern, '', text, flags=re.DOTALL)

    return cleaned_text

def file_saver(input):
    f = open("logs.txt","a")
    f.write(str(input))


if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports":
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    #load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)

    json_pre_book = book

    """
    f = open("yay2.txt","w")
    g = open("yay.txt","w")
    l = open("omg.txt","w")

    f.write(str(json_pre_book))
    g.write(str(json_str_book))
    f.close()
    g.close()
    """
    k = str(json_pre_book)
    k = json.loads(book)

    sys.stdout.write(json.dumps(book))
