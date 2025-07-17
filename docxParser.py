from docx import Document

def read_docx(file_path):
        
    try:
        doc = Document(file_path)
        
        print("\nParsed Content:\n\n")
        for paragraph in doc.paragraphs:
            print(f"{paragraph.text}")
    except Exception as ex:
        print(ex)

read_docx("Communication concepts.docx")
