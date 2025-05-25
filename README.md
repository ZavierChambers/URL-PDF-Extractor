# PDF URL Extractor and Link Generator

This Python script allows you to extract all URLs from a given PDF file and generate a new PDF with clickable hyperlinks. It detects URLs starting with `http://`, `https://`, or `www.` and cleans them for formatting.

---

## 📌 Features

- GUI-based file picker (using `tkinter`)
- Scans the full content of a PDF
- Supports links starting with `http://`, `https://`, or `www.`
- Outputs a clean, clickable PDF with extracted links
- Logs which pages have links and how many were found

---

## 🛠️ Requirements

- Python 3.7+
- Libraries:
  - `PyMuPDF` (`fitz`)
  - `fpdf`
  - `tkinter` (built-in)

Install dependencies:
```bash
pip install pymupdf fpdf
```

---

## 🚀 How to Use

1. Clone or download this repository.
2. Run the script:
   ```bash
   python extract_urls_with_http_https.py
   ```
3. Select a PDF when prompted.
4. Wait for the scan to complete.
5. A new PDF file will be created in the same directory with `_extracted_links.pdf` appended to its name.

---

## 📁 Output

The output is a simple PDF with blue clickable hyperlinks like:
```
http://example.com
https://secure.site/login
www.website.org/page
```

---

## 👤 Author

**Zavier Chambers**  
Cybersecurity & Computer Science Student

---

## 📅 Date

May 25, 2025

---

## 📜 License

This project is licensed under the MIT License.
