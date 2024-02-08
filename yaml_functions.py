import re
import json
import yaml

def return_jekyll_frontmatter(text):
    pattern = r'\A\s*---\s*\n(.*?\n?)---\s*\n'

    front_matter = {}

    match = re.search(pattern, text, flags=re.DOTALL)
    if match: #handling the introduction + blank docs which don't have yaml frontmatter
        front_matter_text = match.group(1)
        cleaned_text = re.sub(pattern, '', text, count=1, flags=re.DOTALL)

        front_matter = yaml.safe_load(front_matter_text)
    else:
        cleaned_text = text

    return front_matter
def remove_jekyll_frontmatter(text):
    pattern = r'^---\s*\n.*?\n---\s*\n'

    # Use re.sub() to replace the front matter with an empty string
    cleaned_text = re.sub(pattern, '', text, flags=re.DOTALL)
    #only remove the first one because that same pattern might appear later - say, if it's an explanation on how frontmatter works, and I don't want that removed.

    return cleaned_text
