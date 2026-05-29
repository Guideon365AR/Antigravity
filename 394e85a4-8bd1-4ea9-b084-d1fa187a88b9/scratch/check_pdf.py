import os

folder = r"c:\Users\Gustavo\Desktop\TD SRP V6 Final"
old_id = b"2104.13856"
new_id = b"2101.10030"

for filename in os.listdir(folder):
    if filename.endswith(".pdf"):
        filepath = os.path.join(folder, filename)
        with open(filepath, "rb") as f:
            data = f.read()
        count = data.count(old_id)
        print(f"{filename}: found {count} occurrences of {old_id.decode()}")
