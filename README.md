
# Parsy: A RAG Powered AI Chatbot

Parsy is a RAG (Retrieval-Augmented Generation) Chatbot which is made with the help of Open Source Large Language Models i.e LLMs like Meta Llama 3 Instruct. This helps user to efficiently get the information from their personal PDF files and answer every question that user have from these personalized PDFs.

The goal is to answer user queries based on a provided
document set (e.g Terms & Conditions, Privacy Policies, Legal Contracts).

## Flow and Architecture

![RAG Application](https://github.com/user-attachments/assets/db4d3462-34a6-4c38-9202-829cc50a5833)

Architecture of a RAG Application:

First we'll parse our desired file ie. pdf and clean our data like removing headers and footers, removing page numbers etc. To make our model more accurate and understand and give answers that are to the point.

Then we'll divide it into chunks. We have different types of chunkings to divide our data into chunks like:
- Fized Size chunkings

In this kind of chunking we neglect the word and semantic meaning of the sentence and just divide it accoding to the length of the characters.

- Sentence-Based Chunkings

In this type, We divide data and separate chunks with "." to get each sentence.

- Recursive Chunkings

Recursive chunking uses a series of separators to iteratively and hierarchically split the input text into smaller parts.

After dividing our file into chunks, We'll convert these chunks into vectors using embedding models like all-MiniLM-L6-v2.

And then We are now going to save these vectors into vector database like Chroma. So that we can retrieve these chunks accoring to the user's query.

Now we'll take the user query and again convert this query to vector for semantic search. So that we can get our top 3 chunks that are highly related to the query of the user.

Now the LLM's work come in the play. LLM will read the user query and analyze our chunks and will generate an answer and display it to the user that answers the user's query and satisfy the user.

## Features

- Uses a vector database for semantic search (Chroma)
- Chunking and embedding documents with sentence-transformers
- LLM Integration with a local inference server (such as Ollama) (LLaMA 3 Instruct)
- The RAG Pipeline Get pertinent pieces → Put into the prompt → Contextual response generation
- Simplified Chat Interface: Responses to live chat input and broadcasting, Sidebar details (total number of chunks, model used), The "Clear Chat" button with personalized design.


## Model And Embeddings

For embeddings:

A dense vector is created from each chunk using model all-MiniLM-L6-v2. To facilitate quick similarity searches, embeddings are kept in a vector database, for that I have used Chroma. 

For LLM:

The main Large Language Model (LLM) used in this project is Meta's LLaMA 3–8B Instruct model, which generates responses depending on retrieved document chunks.


Why LLaMA 3 instruct?

Instruction-oriented: It is perfect for chatbot-style applications like Parsy because it has been trained to follow human-style directions.

High performance: In terms of logic, factuality, and alignment, LLaMA 3 Instruct is one of the best open-weight models.
## Run Parsy Locally

Install dependencies from Requirements.

```bash
  pip install -r requirements.txt
```
Paste your personalized PDF file in the data folder.

Go to the root directory of our chatbot.
And run below command.
```bash
  streamlit run app.py
```
## Screenshots

![Terminal](https://github.com/user-attachments/assets/cd72c44f-195b-4702-aee0-36e347fa488f)
![Chatbot UI](https://github.com/user-attachments/assets/a90d183a-3fbe-4e50-9587-0da599ed692d)
![Processing User Query](https://github.com/user-attachments/assets/35fb8929-bbfb-4eb5-81d4-d8c77a648379)
![Output 1st query](https://github.com/user-attachments/assets/2e9f60d0-519a-43bc-9cd6-e2f4cbde1bf7)
![Output 2st query](https://github.com/user-attachments/assets/7dd4c139-f87e-44f2-a1d5-b4fd3ac15dae)
![Output 3st query](https://github.com/user-attachments/assets/9f1eb98e-d8ec-4540-8b09-4cbc14fc2d4b)

## Video Walthrough

Video Link: https://drive.google.com/file/d/1Nd46zRjOcaL69JCtfgT7aycYdTwHeE9Q/view?usp=sharing

## Authors

- Ashutosh Sharma
    - [Linkedin](https://www.linkedin.com/in/ashutosh-sharma28/)
    - [Github](https://github.com/btw-ImAsh)


