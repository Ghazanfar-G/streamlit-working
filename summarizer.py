
import os 
import google.generativeai as gen
import streamlit as st
gen.configure(api_key=st.secrets["api"])
# Api_Key=st.secrets["api"]
model=gen.GenerativeModel('gemini-1.5-flash-002')
st.title("(●`◡`●)Theory summarizer")
theory=st.text_input("Paste your theory here:")

if st.button("Start"):
    if not theory:
        st.warning('Paste your theory first.')
    else:
        response=model.generate_content(['''Read the theory,and write summary of theory
                                 in such a way that a person after reading it gain knowledge about 
                                 the whole theory.''',theory],stream=True)
        with st.spinner('Loading'):                         
          for chunk in response:
            for words in chunk:
              st.write(words.text)    
