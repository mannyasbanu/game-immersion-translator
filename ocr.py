from PIL import Image
import pytesseract

def extract_text(image_path):
  try:
    # Open image
    img = Image.open(image_path)
    # Extract Japanese text
    text = pytesseract.image_to_string(img, lang='jpn')
    print(f"OCR result:\n{text}")
    # Return string
    return text.strip()
  except Exception as e:
    print(f"OCR failed: {e}")
    return ""
