from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import os
import streamlit as st
import openai
import re

from PIL import Image




page_title = "Prompt Ruuner"
st.set_page_config(
    page_title=page_title,
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "Demo Page by AdCreativeDEv"
    }
)
image = Image.open('openai-banner.png')
st.image(image, caption='created by MJ')

st.title(":blue[" + page_title + "]")


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

with st.sidebar:
    system_openai_api_key = os.environ.get('OPENAI_API_KEY')
    system_openai_api_key = st.text_input(":key: OpenAI Key :", value=system_openai_api_key)
    os.environ["OPENAI_API_KEY"] = system_openai_api_key

    temperature = st.text_input("temperature" ,"0.5") 
    tokens = st.text_input("tokens" ,"200")
    engine =  st.text_input("engine" ,"text-davinci-003")
    

st.subheader("Step 1. 📤 Upload prompt text")

# Define function to read and display text file contents
def upload_file():
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file is not None:
        
        # Read file content
        content = uploaded_file.read().decode("utf-8")

        # SYSTEM PROMPT
        match = re.search(r"\[SYSTEM PROMPT\](.*?)\[USER\]", content, re.DOTALL)
        if match:
            content_system_prompt = match.group(1).strip()
            print(content_system_prompt)
        else:
            content_system_prompt = "Not System Prompt Available !"
        content_system_prompt = st.text_area("SYSTEM PROMPT : ", value=content_system_prompt, height=150)


        # USER PROMPT
        match = re.search(r"\[USER\](.*?)$", content, re.DOTALL)
        if match:
            content_user_prompt = match.group(1).strip()
            print(content_user_prompt)
        else:
            content_user_prompt = ""
        content_user_prompt = st.text_area("USER PROMPT : ", value=content_user_prompt, height=50)




        st.subheader("Step 2 : Submit the Prompt to OpenAI")

        if st.button("Submit to OpenAi"):    
            if  len(content_user_prompt) ==0:
                full_prompt = "System prompt : " + content_system_prompt 
            else:
                full_prompt = "System prompt : " + content_system_prompt + " USER : " + content_user_prompt
            print(full_prompt)
            openai.api_key = system_openai_api_key
            st.spinner("Generating ...")
            completions = openai.Completion.create(
                engine=engine,
                prompt=full_prompt,
                temperature=int(temperature),
                max_tokens=int(tokens),
                top_p=1,
                n=1,
                frequency_penalty=0,
                presence_penalty=0
                )    
            
            replyText = completions['choices'][0]['text']
            st.info(replyText)





# Display file content
upload_file()





    




    


