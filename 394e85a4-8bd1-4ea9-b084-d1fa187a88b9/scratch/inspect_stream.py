import os
from pypdf import PdfReader

folder = r"c:\Users\Gustavo\Desktop\TD SRP V6 Final"
reader = PdfReader(os.path.join(folder, "URLs y Enlaces de Referencias Bibliográficas.pdf"))
page = reader.pages[5]
contents = page.get_contents()
print("Contents object type:", type(contents))
if contents:
    data = contents.get_data()
    print("Contents data length:", len(data))
    print("Is old_id in data?", b"2104.13856" in data)
