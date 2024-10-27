import streamlit as st
from audio_recorder_streamlit import audio_recorder
import torch
import numpy as np
# from langchain import PromptTemplate, LLMChain
from langchain_community.chat_models import ChatOllama
import whisper
from gtts import gTTS
import os
import time
import requests


torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using torch {torch.__version__} ({DEVICE})")


# Using Open AI's whisper small for converting Voice to text
# As I was unable to load the audio file directly to whisper in Windows, I had to create a Rest API  and run it in Ubuntu and transcribe through an API


def transcribe_audio(audio_location):
    url = 'http://localhost:1402/transcribe'
    audio_location = "none"
    audio_path ='/mnt/d/Personal/Experiments/talk_with_AI/Final_voice_assistant/input.mp3'
    data = {'audio_path': audio_path}
    response = requests.post(url, json=data)
    
    # print("Response content:", response.content)  # Print response content
    
    if response.status_code == 200:
        return response.json().get('transcription')
    else:
        print(f'Error: {response.text}')
        return None



# Using Google's Text to Speech to convert the response to an Audio file



def text_to_speech(text):
    language = 'en'
    audioobj = gTTS(text=text, lang=language, slow=False)
    
    # Generate a unique file name based on timestamp
    timestamp = int(time.time())
    file_path = f"output_{timestamp}.mp3"
    
    # Check if the file exists and remove it
    if os.path.exists(file_path):
        os.remove(file_path)

    audioobj.save(file_path)

    return file_path


