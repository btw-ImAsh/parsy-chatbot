
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pickle

def split_texts(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100,
        length_function = len,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(docs)
    pickle.dump(chunks, open('C:\\Users\\jangr\\OneDrive\\Desktop\\AMLgo\\Chatbot\\chunks\\chunks.pkl', 'wb'))
    return chunks