import cv2
import re

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def extract_fields(text):
    fields = {}

    # Extract total
    total_match = re.search(r'(Total|TOTAL|Amount Due|AMOUNT DUE)[^\d]*(\d+\.\d{2})', text)
    if total_match:
        fields['Total'] = total_match.group(2)

    # Extract date
    date_match = re.search(r'(\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2})', text)
    if date_match:
        fields['Date'] = date_match.group(1)

    # Extract name (store/vendor name) — typically the first line
    lines = text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    if lines:
        fields['Vendor'] = lines[0]

    return fields
