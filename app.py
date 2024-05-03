import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.agents import Tool
from langchain_community.tools import YouTubeSearchTool
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv, find_dotenv
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import time
import streamlit as st
import os
from io import StringIO


def main():
    load_dotenv(find_dotenv('.env'))
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    st.set_page_config(page_title="ChatExcel")
    st.header("Ask anything about your Wine Sales! 💰")

    user_file = st.file_uploader("Upload your Excel file here", 
                                 type=["xlsx", "xls", "csv"])

    if user_file:
        llm_gpt4 = ChatOpenAI(temperature=0,
                              api_key=OPENAI_API_KEY,
                              model="gpt-4-turbo")
        
        df_data = pd.read_excel(user_file)
        df_data = df_data.iloc[:-1]
        # csv_buffer = StringIO()
        # excel_data.to_csv(csv_buffer, index=False)
        # csv_buffer.seek(0)
        # print(csv_buffer)
        # print(type(excel_data))

        df_agent = create_pandas_dataframe_agent(llm=llm_gpt4,
                                                 df=df_data,
                                                 return_intermediate_steps=False,
                                                 agent_type="zero-shot-react-description",
                                                 verbose=True)
        
        user_question = st.text_input("Ask a question about your Excel")
        submitted = st.button("Submit Question")
        if submitted:
            st.chat_message("user").write(user_question)
            # st.write(f"Question: {user_question}")
            start_time = time.time()
            st_callback = StreamlitCallbackHandler(st.container())
            response = df_agent.invoke({"input": [user_question]}, 
                                       {"callbacks": [st_callback]})
            # response = {"output":"hi"}
            end_time = time.time()
            elapsed_time = end_time - start_time
            st.write(f"Answer: {response['output']}")
            st.write(f"Elapsed time: {elapsed_time:.2f}s")

if __name__ == "__main__":
    main()