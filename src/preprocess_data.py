
import fitz
from collections import Counter
import re


def parsing_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return [page.get_text() for page in doc]


def detecting_unnecessary(page_texts, min_occur=3):
    counter = Counter()
    for page in page_texts:
        lines = [line.strip() for line in page.split('\n') if line.split()]
        counter.update(lines)

    occured_lines={line for line, count in counter.items() if count>=min_occur}
    return list(occured_lines)


def removing_unnecessary(page_texts):
    cleaned_text = []
    occured_lines= detecting_unnecessary(page_texts)
    for page in page_texts:
        lines = page.split('\n')
        cleaned_lines = [line for line in lines if line.split() not in occured_lines]
        cleaned_text.append('\n'.join(cleaned_lines))
    return " ".join(cleaned_text)


def remove_specials(page_texts):
    page_texts = re.sub(r'Page\s*\d+\s*of\s*\d+', '', page_texts, flags=re.IGNORECASE)
    page_texts = re.sub(r'©\s*\d{4}', '', page_texts)
    page_texts = re.sub(r'\d{1,2}/\d{1,2}/\d{2,4}', '', page_texts)
    page_texts = re.sub(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', '', page_texts)
    
    return page_texts.strip()

