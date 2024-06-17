import speech_recognition as sr
import pygame
from gtts import gTTS
import os
from colorama import init, Fore
import time
from text_handle import text_to_speech,transcribe_audio
from chat import chat_conversation



init()

def record_query():
    # Initialize the recognizer and haulting it for 15 seconds to complete the previous response
    time.sleep(15)
    
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(Fore.YELLOW + "Listening...")
        audio = recognizer.listen(source)

    print(Fore.YELLOW + "Recognizing...")

    try:
        query = recognizer.recognize_google(audio)
        # print(Fore.GREEN + "You said:", query)

        # Save the recorded audio as input.mp3
        with open("input.mp3", "wb") as f:
            f.write(audio.get_wav_data())

        return query
    except sr.UnknownValueError:
        print(Fore.RED + "Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(Fore.RED + "Could not request results; {0}".format(e))
        return None




def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def main():
    while True:
        query = record_query()
        if query is None:
            continue
        elif query.lower() == "bye" or query.lower() == "I am done.":
            print(Fore.YELLOW + "Goodbye!")
            break

        input_audio_file = "input.mp3"
        output_audio_file = "output.mp3"

        user_query = transcribe_audio(input_audio_file)[1:] 
        input = user_query
        print(Fore.GREEN + "You said:", user_query)
        # print("text going to chat is",input)
        response_to_query = chat_conversation.predict(input = input)

        output_audio_file = text_to_speech(text=response_to_query)

        # Play output audio
        play_audio(output_audio_file)

        # Print response
        print(Fore.CYAN + response_to_query)

if __name__ == "__main__":
    main()

    


