def read_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print("\nParsed Content: \n\n")
            print(f.read())
    except Exception as e:
        print(f"\nError reading file: {e}")

read_txt("Communication concepts.txt")
