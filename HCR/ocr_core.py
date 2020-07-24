try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename,lang):
    """
    This function will handle the core OCR processing of images.
    """

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filename),lang=lang)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text  # Then we will print the text in the image
