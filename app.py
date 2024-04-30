import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
import streamlit as st
import os
from io import StringIO

def main():
    load_dotenv()
    st.set_page_config(page_title="ChatExcel")
    st.header("Ask anything about your Wine Sales! 💰")

    user_excel = st.file_uploader("Upload your Excel file here", type=["xlsx", "xls", "csv"])

    if user_excel:
        llm_gpt4 = ChatOpenAI(temperature=0, 
                              model="gpt-4-turbo")
        
        excel_data = pd.read_excel(user_excel)
        excel_data = excel_data.iloc[:-1]
        csv_buffer = StringIO()
        excel_data.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        csv_agent = create_csv_agent(llm=llm_gpt4, 
                                     path=csv_buffer, 
                                     verbose=True)
        
        user_question = st.text_input("Ask a question about your Excel")
        submitted = st.button("Submit Question")
        if submitted:
            # st.write(f"Question: {user_question}")
            response = csv_agent.invoke(user_question)
            st.write(f"Answer: {response['output']}")

if __name__ == "__main__":
    main()