import streamlit as st
from gtts import gTTS
from playsound import playsound

st.title("TTS with gTTS and Streamlit")


user_input = st.text_area("Enter text for TTS:", "Type here...")

if st.button("Convert to Speech"):
    filename = "sunny1.mp3"
    x = gTTS(text=user_input, lang='ko')
    x.save(filename)
    
    st.audio(filename, format='audio/mp3')
 










    
      
