import streamlit as st
from streamlit_lottie import st_lottie
import json
import ollama
import pyttsx3
engine = pyttsx3.init()
with open("D:\\assistant web app\\AI_animation.json","r") as file:
    url = json.load(file)
st_lottie(url,height=500)
prompt = st.chat_input("Ask anything....")
if prompt:
    response = ollama.chat(model="gemma:2b",messages=[{'role': 'user','content': prompt}])
    answer = response["message"]["content"]
    engine.say(answer)
    engine.runAndWait()