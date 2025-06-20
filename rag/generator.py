from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import requests
import warnings

warnings.filterwarnings("ignore",category=DeprecationWarning)

embedding_model = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
CHROMA_PATH='C:\\Users\\jangr\\OneDrive\\Desktop\\AMLgo\\Chatbot\\vectorDB'

try:
    def run_llama3_instruct(prompt):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:instruct",
                "prompt": prompt,
                "stream": False
            }
        )
        data = response.json()
        return data['response']
except Exception as e:
    print(f"Failed to run Llama 3 Instruct: {e}")

db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_model)

def ans_by_context(context, question):
    prompt=f'''
    Answer the questions only based on the following context:
    {context}

    -----
    Answer the question based on the above context: {question}
    '''
    response = run_llama3_instruct(prompt)
    return response

def generate_answers(user_query):
    results = db.similarity_search_with_relevance_scores(user_query, k=5)
    content_texts = "\n\n----\n\n".join([doc.page_content for doc, _score in results])
    ans_by_llm = ans_by_context(content_texts, user_query)
    return ans_by_llm
