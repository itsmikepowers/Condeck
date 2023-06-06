import os
import json
from google.cloud import speech_v1p1beta1 as speech
from pydub import AudioSegment
from google.oauth2 import service_account
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Set Google Cloud service account credentials
credentials = service_account.Credentials.from_service_account_file("./Assets/code.json")

# Convert mp3 file to wav
audio = AudioSegment.from_mp3("audio.mp3")
audio.export("audio.wav", format="wav")

# Open audio file
with open("audio.wav", "rb") as audio_file:
    audio_content = audio_file.read()

# Prepare API request
client = speech.SpeechClient(credentials=credentials)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code="en-US",
    enable_word_time_offsets=True,
    model="video",  
    enable_automatic_punctuation=True, 
    diarization_config=speech.SpeakerDiarizationConfig(
        enable_speaker_diarization=True,  
        min_speaker_count=1,
        max_speaker_count=6,
    ),
)
audio = speech.RecognitionAudio(content=audio_content)

# Transcribe audio
response = client.recognize(config=config, audio=audio)

# Prepare the JSON structure
transcript = []
for i, result in enumerate(response.results):
    if i > 0:  # Only process the first result
        break
    alternative = result.alternatives[0]  # Consider only the first alternative
    for word_info in alternative.words:
        word_dict = {
            'index': i,
            'word': word_info.word.capitalize(),  # Capitalize the first letter
            'start_time': word_info.start_time.total_seconds(),
            'end_time': word_info.end_time.total_seconds()
        }
        transcript.append(word_dict)

# Save JSON file
with open('transcript.json', 'w') as json_file:
    json.dump(transcript, json_file, indent=4)

# Load the video file
video = VideoFileClip('final_video.mp4')

# List to hold subtitle clips
subs = []

# Process each transcript item
for item in transcript:
    # Create a TextClip for each item
    txt_clip = (TextClip(item["word"], fontsize=140, color='white', font=r'C:\Users\mikep\AppData\Local\Microsoft\Windows\Fonts\Poppins-Bold.ttf', stroke_color='black', stroke_width=7)
                .set_position('center')
                .set_duration(item["end_time"] - item["start_time"])
                .set_start(item["start_time"]))

    # Add TextClip to the list
    subs.append(txt_clip)

# Overlay subtitles on the video
video = CompositeVideoClip([video] + subs)

# Write the result to a file
video.write_videofile("final_video_captions.mp4")




import os

def rename_file(old_name, new_name):
    # if the target file already exists, remove it
    if os.path.exists(new_name):
        os.remove(new_name)
        print(f"A file named {new_name} already exists, it will be overwritten.")
    
    # check if the original file exists
    if os.path.exists(old_name):
        # rename the file
        os.rename(old_name, new_name)
        print(f"File has been renamed from {old_name} to {new_name}")
    else:
        print("File does not exist, please enter a valid file name")

old_name = 'final_video_captions.mp4'
new_name = 'final_video.mp4'

rename_file(old_name, new_name)
