# 🧾 Receipt OCR Parser

This project uses Python, OpenCV, and Tesseract OCR to extract important information (like vendor name, date, and total amount) from receipt images.

## 📸 Example Use Case

Imagine you scan a receipt and want to automatically log the vendor name, total amount, and purchase date — this script does exactly that.

---

## 🛠️ Features

- Image preprocessing with OpenCV
- Optical Character Recognition using Tesseract
- Regular expression-based extraction of:
  - **Vendor name**
  - **Total amount**
  - **Date**

---

## 📂 Project Structure

```bash

├── main.py            # Entry point of the application
├── utils.py           # Helper functions for preprocessing and data extraction
└── utils.cpython-312.pyc # Compiled helper file (optional, can be ignored on GitHub)
```

## 🚀 Getting Started
Prerequisites
Python 3.x

Tesseract OCR installed on your system

Required Python packages: OpenCV, pytesseract

Installation
Clone this repository:

```
git clone https://github.com/yourusername/receipt-ocr-parser.git
cd receipt-ocr-parser
```
Install dependencies:

```
pip install opencv-python pytesseract
```
Update the path to tesseract.exe in main.py:

```
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
Place your receipt image and update image_path in main.py accordingly.

## 🧪 Run the Script

python main.py
This will print both the full OCR output and the extracted fields.

## 📝 Output Example

Full OCR Result:
WALMART STORE
...
Total: 23.45
Date: 12/03/2024

Extracted Fields:
{'Vendor': 'WALMART STORE', 'Total': '23.45', 'Date': '12/03/2024'}


## 📌 Notes
The script uses basic regex and may not work perfectly with all receipts. Feel free to improve the logic in utils.py.

This is a minimal prototype — consider integrating NLP or ML for better field extraction.
