from src.preprocess_data import parsing_pdf, removing_unnecessary, remove_specials
from src.chunks import split_texts
from src.vectordb import save_to_db
from langchain.schema import Document

file_path='C:\\Users\\jangr\\OneDrive\\Desktop\\AMLgo\\Chatbot\\data\\AI_Training_Document.pdf'

def main():
    
    page_texts = parsing_pdf(file_path)
    page_texts = removing_unnecessary(page_texts)
    page_texts = remove_specials(page_texts)
    docs = [
        Document(page_content=page_texts)
    ]
    chunks = split_texts(docs)

    save_to_db(chunks)

if __name__ == "__main__":
    main()
