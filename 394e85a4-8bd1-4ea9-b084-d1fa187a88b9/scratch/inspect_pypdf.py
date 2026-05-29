from pypdf import PdfReader
reader = PdfReader(r"c:\Users\Gustavo\Desktop\TD SRP V6 Final\URLs y Enlaces de Referencias Bibliográficas.pdf")
page = reader.pages[0]
print("Page attributes:", dir(page))
contents = page.get_contents()
if contents:
    print("Contents type:", type(contents))
    if isinstance(contents, list):
        print("First content attributes:", dir(contents[0]))
    else:
        print("Content attributes:", dir(contents))
