from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import os
import streamlit as st
from io import StringIO 

from PIL import Image

# image = Image.open('story.png')



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
# st.image(image, caption='created by midjourney ')
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

st.subheader("Step 1. 📤 Upload prompt text")

# Define function to read and display text file contents
def upload_file():
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file is not None:
        # Read file content
        text = uploaded_file.read().decode("utf-8")
        return text





# Display file content
st.subheader("File Content")
st.text_area("Text", value=upload_file(), height=600)





    




    


