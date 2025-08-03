import os
import pandas as pd
import streamlit as st
from pandasai import Agent

# Set your API key for BambooLLM
os.environ["PANDASAI_API_KEY"] = "YOUR KEY HERE"  # <--- Paste your API key Generated from Pandasai Wesbite , Use Readme file for more info.

# Streamlit app
def main():
    st.title("Library Assistant")

    chat_container = st.container()

    with st.sidebar:
        uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    with chat_container:
        st.header("Find your Books")
        query = st.text_input("Ask a question about the data:")

    if uploaded_file is not None:
        books = pd.read_csv(uploaded_file)
        agent = Agent(books)

        if query:
            response = agent.chat(query)
            with chat_container:
                st.write("### Response:")
                st.write(response)

if __name__ == "__main__":
    main()