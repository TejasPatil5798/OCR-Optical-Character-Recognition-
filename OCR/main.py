import cv2
import pytesseract
from utils import preprocess_image, extract_fields

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Load image
image_path = 'E:/Cursor demos/Demo2/OCR/image.png'
image = cv2.imread(image_path)

# Preprocess image
processed_img = preprocess_image(image)

# OCR using pytesseract
ocr_result = pytesseract.image_to_string(processed_img)

# Print full OCR text (optional)
print("Full OCR Result:\n", ocr_result)

# Extract specific fields
fields = extract_fields(ocr_result)
print("\nExtracted Fields:\n", fields)
