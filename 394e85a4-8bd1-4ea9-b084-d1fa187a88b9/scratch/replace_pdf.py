import os
from pypdf import PdfReader, PdfWriter

folder = r"c:\Users\Gustavo\Desktop\TD SRP V6 Final"
old_id = "2104.13856"
new_id = "2101.10030"

def replace_in_pdf(filepath):
    print(f"Processing {filepath}...")
    reader = PdfReader(filepath)
    writer = PdfWriter()
    
    replaced_count = 0
    
    for i, page in enumerate(reader.pages):
        # Decompress content streams to make text editable in raw format
        page.decompress_content_streams()
        
        # Check if the content stream exists and modify it
        contents = page.get_contents()
        if contents:
            # get_contents can return a list or a single stream
            if not isinstance(contents, list):
                contents = [contents]
            
            for content in contents:
                data = content.get_data()
                # Try replacing both as string and bytes
                if old_id.encode('utf-8') in data:
                    new_data = data.replace(old_id.encode('utf-8'), new_id.encode('utf-8'))
                    content.set_data(new_data)
                    replaced_count += 1
                    print(f"  Page {i+1}: Replaced in content stream.")

        # Check and replace in annotations (like links /URI)
        if "/Annots" in page:
            annots = page["/Annots"]
            # annots could be an array of indirect objects
            for annot_ref in annots:
                annot = annot_ref.get_object()
                if "/A" in annot:
                    action = annot["/A"].get_object()
                    if "/URI" in action:
                        uri = action["/URI"]
                        if old_id in uri:
                            action.update({
                                "/URI": uri.replace(old_id, new_id)
                            })
                            replaced_count += 1
                            print(f"  Page {i+1}: Replaced in URI annotation.")
                            
        writer.add_page(page)
        
    # Also search and replace in raw document catalog or metadata if needed
    # But doing it page-by-page is usually enough for citations and links.
    
    if replaced_count > 0:
        backup_path = filepath + ".bak"
        if not os.path.exists(backup_path):
            os.rename(filepath, backup_path)
            print(f"  Saved backup to {backup_path}")
        else:
            os.remove(filepath)
            
        with open(filepath, "wb") as f:
            writer.write(f)
        print(f"  Successfully wrote updated PDF to {filepath} ({replaced_count} replacements made).")
    else:
        print(f"  No replacements made in {filepath}.")

for filename in os.listdir(folder):
    if filename.endswith(".pdf") and not filename.endswith(".bak"):
        filepath = os.path.join(folder, filename)
        try:
            replace_in_pdf(filepath)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
