import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
import streamlit as st
import os

def main():
    st.set_page_config(page_title="ChatCSV")
    st.header("Ask anything about your Wine Sales! 💰")

    st.file_uploader("Upload your Excel file here")

if __name__ == "__main__":
    main()
