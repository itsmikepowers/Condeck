import requests
import os
from pydub import AudioSegment
import sys

audio_text = sys.argv[1]

def convert_text_to_speech(api_key, voice_id, text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        with open("audio.mp3", "wb") as file:
            file.write(response.content)
        
        # Load audio file
        audio = AudioSegment.from_file("audio.mp3")

        # Increase volume by 10 dB
        louder_audio = audio + 2

        # Export audio file
        louder_audio.export("audio.mp3", format='mp3')
        print("Audio Generated and volume increased!")
    else:
        print(f"Request failed with status code {response.status_code}")
        
api_key = "YOUR API KEY HERE"
voice_id = "YOUR VOICE ID HERE"
text = audio_text

convert_text_to_speech(api_key, voice_id, text)
