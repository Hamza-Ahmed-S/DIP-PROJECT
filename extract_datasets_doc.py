from docx import Document

# Read the datasets Word document
doc = Document(r"D:\Others\VS CODE\DIP PROJECT\Project Group-12  Dataset\Datasets for Bioinformatics using Python.docx")

# Extract all text and save to file
with open("datasets.txt", "w", encoding="utf-8") as f:
    f.write("=" * 80 + "\n")
    f.write("BIOINFORMATICS DATASETS\n")
    f.write("=" * 80 + "\n\n")
    
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            f.write(paragraph.text + "\n")
    
    f.write("\n" + "=" * 80 + "\n")

print("Datasets extracted to datasets.txt")
