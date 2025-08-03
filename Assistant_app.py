import os
import pandas as pd
import streamlit as st
from pandasai import Agent

os.environ["PANDASAI_API_KEY"] = "YOUR API KEY" # <--- Paste your API key Generated from Pandasai Wesbite , Use Readme file for more info.

def main():
    st.markdown(
        """
        <h1 style="text-align: center;">
            Library Assistant
        </h1>
        """,
        unsafe_allow_html=True
    )

    chat_container = st.container()

    with st.sidebar:
        uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    with chat_container:
        st.header("Find your Books")

        if uploaded_file is not None:
            query = st.text_input("Ask a question about the data:")

            with st.spinner("Please wait..."):
                books = pd.read_csv(uploaded_file)
                agent = Agent(books)

                if query:
                    response = agent.chat(query)
                    st.write("### Response:")
                    st.write(response)
        else:
            st.write("Upload a CSV file to start.")
            st.write("Once the file is uploaded, you will be able to ask questions about the data.")

if __name__ == "__main__":
    main()
