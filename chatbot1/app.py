import streamlit as st
import gdown
from llama_index import StorageContext, load_index_from_storage, ServiceContext
from llama_index.llms import HuggingFaceInferenceAPI
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.chat_engine import ContextChatEngine, ChatMemoryBuffer
from llama_index.schema import ChatMessage, MessageRole

# Load secrets
token = st.secrets["hf_token"]

# Download vector database folder from Google Drive
@st.cache_resource
def download_vector_db():
    gdown.download_folder("1ykKlRQH7wXBl9P1YHAOVUfcfVs0PpNRs", quiet=False, use_cookies=False)

# Load LLM, Embedding, and Index
@st.cache_resource
def setup_chatbot():
    hf_model = "mistralai/Mistral-7B-Instruct-v0.3"
    embedding_model = "sentence-transformers/all-MiniLM-l6-v2"

    llm = HuggingFaceInferenceAPI(model_name=hf_model, task="text-generation", token=token)
    embeddings = HuggingFaceEmbedding(model_name=embedding_model)

    storage_context = StorageContext.from_defaults(persist_dir="./vector_index_2")
    vector_index = load_index_from_storage(storage_context, embed_model=embeddings)
    retriever = vector_index.as_retriever(similarity_top_k=2)

    prompts = [
        ChatMessage(role=MessageRole.SYSTEM, content="You are a nice chatbot having a conversation with a human."),
        ChatMessage(role=MessageRole.SYSTEM, content="Answer the question based only on the following context and previous conversation."),
        ChatMessage(role=MessageRole.SYSTEM, content="Keep your answers short and succinct."),
        ChatMessage(role=MessageRole.SYSTEM, content="Dont respond to user and assistant.")
    ]

    memory = ChatMemoryBuffer.from_defaults()
    chat_engine = ContextChatEngine(
        llm=llm,
        retriever=retriever,
        memory=memory,
        prefix_messages=prompts
    )
    return chat_engine

# Streamlit UI
st.title("Alice's Adventures Chatbot")
st.info("Ask anything about the book. Type 'end' to stop.")

# Initial download
download_vector_db()

chat_engine = setup_chatbot()

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")

if user_input.lower() == "end":
    st.write("👋 Ending the conversation. Goodbye!")
elif user_input:
    response = chat_engine.chat(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response.response))

# Display chat history
for role, message in st.session_state.history:
    st.markdown(f"**{role}:** {message}")
