import json

file_path = "Text_to_img.ipynb"

with open(file_path, "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Remove problematic metadata
if "metadata" in notebook:
    notebook["metadata"].pop("widgets", None)

for cell in notebook.get("cells", []):
    cell.get("metadata", {}).pop("widgets", None)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print("✅ Cleaned widget metadata from:", file_path)
