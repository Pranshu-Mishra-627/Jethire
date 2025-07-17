from PIL import Image
import pytesseract

try:
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Pythonn\\tesseract\\tesseract.exe"
    image_path = 'resume.jpg'
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)

    print(extracted_text)
except Exception as ex:
    print(ex)