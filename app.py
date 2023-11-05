import streamlit as st
from src.utils import *

# Some CSS styling (removing made with streamlit)
css = """
<style>
.st-emotion-cache-h5rgaw  {
    font-size: 0px;
}"""
st.markdown(css, unsafe_allow_html=True)

# App
st.title('🎬🔗 Video Summarizer')
url = st.text_input('Plug in your video link here')

if url:
    transcript = transcript_loader(url)
    output = summarizer(transcript)
    st.markdown(output) 