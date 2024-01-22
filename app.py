import streamlit as st 
from io import StringIO
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

from prompts import assistant_prompt

# Constants
PAGE_TITLE = "CodeElevate AI"
PAGE_ICON = "🛸"
OPENAI_MODEL_NAME = "gpt-4"
OPENAI_API_KEY_PROMPT = 'OpenAI API Key'
FILE_UPLOAD_PROMPT = "Upload your python file here"
FILE_UPLOAD_TYPE = ".py"
ASSISTANT_PROMPT = assistant_prompt

# Set page config
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, initial_sidebar_state="collapsed")

st.header("",divider='blue')
st.title(f"🛸 :blue[_{PAGE_TITLE}_] | Code Reviewer")
st.header("",divider='blue')
# Get OpenAI API key
openai_api_key = st.sidebar.text_input(OPENAI_API_KEY_PROMPT, type='password')

if not openai_api_key.startswith('sk-'):
    st.info("Please add your OpenAI API key in the sidebar to continue.")
    st.stop()

with st.sidebar:
        
    st.divider()
    
    st.write('*Your EchoLogic Adventure begins with a Python file.*')
    st.caption('''**That's why I'd love for you to upload a Python file. 
               Once we have your code, we'll understand it and start exploring it.
                Then, we'll work together to shape your code file.  
                Sounds fun, right?**
    ''')

    st.divider()


# File uploader
user_file = st.file_uploader(FILE_UPLOAD_PROMPT, type=FILE_UPLOAD_TYPE)

if user_file: 
    decoded = StringIO(user_file.getvalue().decode('utf-8'))
    contents = decoded.read()
    st.divider()
    st.subheader("Uploaded File:")
    st.code(contents, line_numbers=True)
    st.divider()
    
    st.subheader("Recommendations: ")
    with st.spinner('Please wait...'):
        chat = ChatOpenAI(model_name=OPENAI_MODEL_NAME, temperature=0.9, openai_api_key=openai_api_key)
        assistant_text = SystemMessage(content= ASSISTANT_PROMPT)
        user_text = HumanMessage(content = contents)

        response = chat([assistant_text, user_text])

        st.write(response.content)
        st.divider()