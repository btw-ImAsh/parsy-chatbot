import streamlit as st
import os
try:
    from rag.generator import generate_answers
except Exception as e:
    st.error(f"Failed to import generator: {e}")
    st.stop()
from retriever import main
import pickle as pk

st.markdown("""
    <style>
        /* Main app background and font */
        .stApp {
            background-color: white !important;
            color: black;  /* Default font color */
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background: linear-gradient(90deg, rgba(151, 222, 248, 1) 0%, rgba(238, 204, 254, 1) 85%);
            color: black !important;
        }

        
        /* Ensure all markdown and text elements have black font */
        .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader {
            color: black !important;
        }
        section[data-testid="stSidebar"] button{
            background-color: transparent !important;
            color: black !important;
            border: 1.5px solid black !important;
            border-radius: 8px !important;
            transition: background-color 0.3s ease;
        }
        section[data-testid="stSidebar"] button:hover {
            background: linear-gradient(90deg,rgba(151, 222, 248, 1) 43%, rgba(238, 204, 254, 1) 94%);
            color: black !important;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)


st.set_page_config(page_title="RAG Chatbot", layout='wide')
Chunks_path = 'C:\\Users\\jangr\\OneDrive\\Desktop\\AMLgo\\Chatbot\\chunks\\chunks.pkl'

if os.path.exists(Chunks_path):
    pass
else:
    main()

try:
    chunks = pk.load(open(Chunks_path, 'rb'))
except Exception as e:
    st.error(f"Failed to load chunks.pkl: {e}")
    st.stop()


with st.sidebar:
    st.title("🔍 Parsy: A RAG Chatbot")
    st.write("Model: `Llama-3-8B-Instruct`")
    st.write(f"📄 Indexed Chunks: {len(chunks)}")
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []

st.image('C:\\Users\\jangr\\OneDrive\\Desktop\\AMLgo\\Chatbot\\chatbot-logo.png', width=80)

st.title('Need Answers❓ Ask to Parsy.')
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

user_query = st.chat_input('Shoot Your Ques Here...')

if user_query:
    st.chat_message('user').markdown(user_query)
    st.session_state.messages.append({'role': 'user', 'content': user_query})
    try:
        with st.spinner("Generating answer..."):
            response = generate_answers(user_query)
    except Exception as e:
        response = f"❌ Error while generating response: {e}"
        st.error(response)
    st.chat_message('assistant').markdown(response)
    st.session_state.messages.append({'role':'assistant', 'content': response})
