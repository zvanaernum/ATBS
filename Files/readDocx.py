#! python3
# creating a function to get plaintext from a word document
from docx import Document

def getText(filename):
    doc = Document(filename)
    fullText = []
    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)
    return '\n'.join(fullText)