import fitz 

def read_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        print("\nParsed Content: \n\n")
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            print(f"\nPage {page_num + 1}:\n{text}")
    except Exception as ex:
        print(ex)

read_pdf("Communication concepts.pdf")