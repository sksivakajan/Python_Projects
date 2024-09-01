import tkinter as tk
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import threading

# Function to recognize speech from the microphone
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        try:
            # Listen and recognize speech
            audio_data = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio_data)
            output_text.set(text)
            status_label.config(text="Recognition Complete")
        except sr.UnknownValueError:
            output_text.set("Sorry, I could not understand the speech.")
        except sr.RequestError:
            output_text.set("Error with the speech recognition service.")
        except sr.WaitTimeoutError:
            output_text.set("Listening timed out.")

# Function to convert text to speech using gTTS
def text_to_speech():
    text = output_text.get()
    if text:
        tts = gTTS(text, lang='en')
        audio = BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)
        sound = AudioSegment.from_file(audio, format="mp3")
        play(sound)

# Threaded execution for speech recognition
def threaded_recognition():
    threading.Thread(target=recognize_speech).start()

# Creating the GUI
root = tk.Tk()
root.title("AI Speech Recognition")

# Output Text Variable
output_text = tk.StringVar()

# Title Label
title_label = tk.Label(root, text="AI Speech Recognition & Speech-to-Text", font=("Helvetica", 16))
title_label.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Click 'Start' to begin speech recognition", font=("Helvetica", 12))
status_label.pack(pady=10)

# Start Button
start_button = tk.Button(root, text="Start", command=threaded_recognition, font=("Helvetica", 14), bg="lightblue")
start_button.pack(pady=10)

# Display the recognized text
recognized_text_label = tk.Label(root, textvariable=output_text, font=("Helvetica", 14), wraplength=400)
recognized_text_label.pack(pady=10)

# Speak Button to convert the text to speech
speak_button = tk.Button(root, text="Speak", command=text_to_speech, font=("Helvetica", 14), bg="lightgreen")
speak_button.pack(pady=10)

# Start the Tkinter main loop
root.geometry("500x300")
root.mainloop()
