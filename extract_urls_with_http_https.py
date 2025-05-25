"""
extract_urls_with_http_https.py

Description:
    This script extracts all URLs from a selected PDF file and generates a new PDF with clickable links.
    It supports URLs starting with http://, https://, or www.

Usage:
    1. Run the script.
    2. A file dialog will prompt you to select a PDF file.
    3. The script scans each page for URLs, logs findings to the console, and collects them.
    4. A new PDF named <original_filename>_extracted_links.pdf is created with each URL rendered as a clickable link.

Author: Zavier Chambers (IT Guy)
Date: 2025-05-25
Version: 1.0
License: MIT

"""

import fitz  # PyMuPDF
import re
import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF
import os


def extract_urls_from_pdf(pdf_path):
    # Match any sequence starting with http://, https://, or www. up to whitespace
    raw_pattern = re.compile(r'(?:https?://|www\.)\S+')
    doc = fitz.open(pdf_path)
    all_links = set()
    total = doc.page_count

    for i in range(total):
        page = doc.load_page(i)
        text = page.get_text("text")
        found = raw_pattern.findall(text)

        cleaned = []
        for r in found:
            # strip trailing punctuation
            link = r.rstrip('.,;:)]}\"\'')
            cleaned.append(link)

        if cleaned:
            print(f"[Page {i+1}/{total}] → found {len(cleaned)} link(s): {cleaned}")
        else:
            print(f"[Page {i+1}/{total}] → no links found")

        all_links.update(cleaned)

    doc.close()
    return sorted(all_links)


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Clickable URLs Extracted from PDF', ln=1, align='C')


def create_clickable_pdf(urls, output_file):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for url in urls:
        # Ensure full URL has http scheme
        full_url = url if url.startswith(("http://","https://")) else f"http://{url}"
        pdf.set_text_color(0, 0, 255)
        pdf.cell(0, 10, url, ln=1, link=full_url)

    pdf.output(output_file)
    print(f"\n✅ Clickable PDF saved as: {output_file}")


def select_pdf_and_create_link_pdf():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not file_path:
        print("No file selected.")
        return

    print(f"Opening {os.path.basename(file_path)}…")
    urls = extract_urls_from_pdf(file_path)

    if not urls:
        print("\nNo URLs found in the entire document.")
        return

    output_file = os.path.splitext(file_path)[0] + "_extracted_links.pdf"
    create_clickable_pdf(urls, output_file)


if __name__ == "__main__":
    select_pdf_and_create_link_pdf()
