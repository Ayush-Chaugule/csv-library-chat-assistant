# Library AI Assistant

A smart Streamlit-based chatbot that helps users explore library datasets using natural language, powered by [PandasAI](https://pandas-ai.com/).

Learn more about PandasAI in the [official documentation](https://docs.pandas-ai.com/).

Generate a free PandaiAI API key at (https://app.pandabi.ai)

---

## Features

- Upload your own `.csv` library file
- Ask natural language questions like:
  - "How many books are available?"
  - "List all books by 'xyz' author"
- Built with:
  - `pandas`
  - `streamlit`
  - `pandasai`

---

## Demo Data

A sample CSV is included: `Sample_Data.csv`  
Feel free to replace it with your own.

---

## Note!
Tested on Python 3.10.0. 
Other versions may cause compatibility issues or throw errors.

---

## Installation

```bash
pip install -r requirements.txt
streamlit run Assistant_app.py


