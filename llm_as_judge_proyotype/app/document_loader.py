# app/document_loader.py

import docx
import re
from typing import Dict

def load_and_split_document(file_path: str) -> Dict[str, str]:
    """
    Loads a DOCX document and splits it into sections based on headings like '1.', '2.', etc.
    Returns a dictionary: {section_title: section_content}
    """
    document = docx.Document(file_path)
    full_text = "\n".join([para.text.strip() for para in document.paragraphs if para.text.strip()])

    # Split based on numbered headings like "1. Introduction", "2. Business Requirements"
    sections = re.split(r'(?=(\d+\.\s+[A-Z][^\n]+))', full_text)

    # sections = ['', '1. Introduction', 'Content...', '2. Business Requirements', 'Content...']
    result = {}
    i = 1
    while i < len(sections) - 1:
        title = sections[i].strip()
        content = sections[i+1].strip()
        result[title] = content
        i += 2
    return result

# Add this to the bottom of app/document_loader.py
"""
if __name__ == "__main__":
    import os

    # Example DOCX path (adjust if your filename is different)
    file_path = os.path.join("data", "FDD_PR_Approval_Report.docx")

    print(f"📄 Loading and splitting document: {file_path}\n")
    sections = load_and_split_document(file_path)

    for title, content in sections.items():
        print(f"=== {title} ===")
        print(content[:500])  # Print first 500 chars of content
        print("\n" + "-" * 80 + "\n")

"""