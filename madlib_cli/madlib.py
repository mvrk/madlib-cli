import re
import pytest


def read_template(path):
    with open(path, 'r') as f:
        content = f.read().strip()
        return content


def parse_template(content):
    parts = []
    string = re.findall(r'\{.*?\}', content)
    text = re.sub("{[^}]*}", "{}", content)
    for i in string:
        parts.append(i.strip("{ }"))
    return text, tuple(parts)


def merge(text, words):
    newstr = text.format(*words)
    return newstr


def welcome_msg():
    text = """
    **************************************************************
    **     Welcome to Mad Libs, where every word makes          **
    **     sense. You will be promote to type in words          **
    **     and code give you an random story.                   **
    **     Let's play and have fun!                             **
    **************************************************************
    """
    print(text)


def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()


welcome_msg()

template_file = read_template('assets/dark_and_stormy_night_template.txt')
stripped, parts = parse_template(template_file)
responses = []
for x in parts:
    print(f"Enter a {x}")
    response = input("> ")
    responses.append(response)
answer = merge(stripped, tuple(responses))
print(answer)

f = open("answer.txt", "w")
f.write(answer)
f.close()
