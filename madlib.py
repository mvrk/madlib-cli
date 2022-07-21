import re

print("Welcome to 401lab03, madlib!")


# READ files from directories.
def read_template(path):
    with open(path, 'r') as f:
        content = f.read().strip()
        return content


def parse_template(content):
    parts = []
    string = re.findall(r'\{.*?\}', content)  # find all words between{}
    text = re.sub("{[^}]*}", "{}", content)  # remove them
    for i in string:
        parts.append(i.strip("{ }"))
    return text, tuple(parts),


def merge(text, words):
    var = text.format(*words)
    return var
