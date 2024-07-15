import markdown

with open('readme.md', 'r') as file:
    text = file.read()
    html = markdown.markdown(text)

    print(html)

