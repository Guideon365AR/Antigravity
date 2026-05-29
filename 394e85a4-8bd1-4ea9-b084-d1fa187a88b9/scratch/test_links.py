import os
from pypdf import PdfReader, PdfWriter

folder = r"c:\Users\Gustavo\Desktop\TD SRP V6 Final"
old_id = "2104.13856"
new_id = "2101.10030"

reader = PdfReader(os.path.join(folder, "URLs y Enlaces de Referencias Bibliográficas.pdf"))
page = reader.pages[5] # page 6

print("Page has /Annots:", "/Annots" in page)
if "/Annots" in page:
    annots = page["/Annots"]
    for annot_ref in annots:
        annot = annot_ref.get_object()
        print("Annot:", annot)
        if "/A" in annot:
            action = annot["/A"].get_object()
            print("Action:", action)
            if "/URI" in action:
                uri = action["/URI"]
                print("URI:", uri)
                if old_id in uri:
                    print("Found in URI!")
