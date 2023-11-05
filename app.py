import streamlit as st
from src.utils import *

st.title('😁🔗 Video Summarizer')
url = st.text_input('Plug in your video link here')

if url:
    transcript = transcript_loader(url)
    output = summarizer(transcript)
    st.write(output) 