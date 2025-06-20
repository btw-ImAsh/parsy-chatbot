from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import warnings

warnings.filterwarnings("ignore",category=DeprecationWarning)

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

CHROMA_PATH='C:\\Users\\jangr\\OneDrive\\Desktop\\AMLgo\\Chatbot\\vectorDB'

def save_to_db(chunks):
    db = Chroma.from_documents(chunks, embedding=embedding_model, persist_directory=CHROMA_PATH)
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")
