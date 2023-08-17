# Code-to-connect-ChatGPT-to-answer-questions
#Libraries
import speech_recognition as sr
from gtts import gTTS
import os
import openai
# Set your OpenAI API key here
openai.api_key = "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"
# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()
# Listen for audio from the microphone
with sr.Microphone() as source:
print("Say something...")
audio = recognizer.listen(source)
try:
# Extract text from audio using the Google Web Speech API
text = recognizer.recognize_google(audio, language='en')
print("Recognized text: " + text)
except sr.UnknownValueError:
print("Speech not recognized")
except sr.RequestError as e:
print("Error retrieving data from Google Web Speech API: {0}".format(e))
# Use the recognized text as input for the OpenAI engine to generate text
response = openai.Completion.create(
engine="text-davinci-003",  # Use the appropriate engine (e.g., text-davinci-003)
prompt=text,
max_tokens=50
)
# Extract the generated text from the OpenAI engine outputs
answer = response.choices[0].text.strip()
print("Response:", answer)
# Generate an audio file from the text using gTTS and save it as an MP3 file
tts = gTTS(answer, lang='en')
tts.save("gpt_response.mp3")
# Play the audio files using the os.system command
os.system("start output.mp3")
os.system("start gpt_response.mp3")
