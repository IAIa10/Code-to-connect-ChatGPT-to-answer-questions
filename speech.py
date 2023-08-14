import speech_recognition as sr
from gtts import gTTS
import os
import openai


openai.api_key = "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"


recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google(audio, language='en')
    print("Recognized text: " + text)
except sr.UnknownValueError:
    print("Speech not recognized")
except sr.RequestError as e:
    print("error retrieving data from Google Web Speech API; {0}".format(e))

response = openai.Completion.create(
    engine="text-davinci-003",  # Use the appropriate engine (e.g., text-davinci-003)
    prompt=text,
    max_tokens=50
)


answer = response.choices[0].text.strip()

print("Response:", answer)
tts = gTTS(answer, lang='en')
tts.save("gpt_response.mp3")
os.system("start output.mp3")
os.system("start gpt_response.mp3")
