from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def add_audio_to_video(video_path, audio_path, output_path):
    # Load video clip
    video = VideoFileClip(video_path)
    video_audio = video.audio

    # Load audio file
    audio = AudioFileClip(audio_path)

    # Adjust audio to video duration
    audio = audio.audio_loop(duration=video.duration)

    # Composite audio clips
    composite_audio = CompositeAudioClip([video_audio, audio])

    # Set audio to the video clip
    video = video.set_audio(composite_audio)

    # Write the result to a file
    video.write_videofile(output_path, codec='libx264')

add_audio_to_video('final_video.mp4', './Assets/Music/1.1.wav', 'final_video_music.mp4')





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

old_name = 'final_video_music.mp4'
new_name = 'final_video.mp4'

rename_file(old_name, new_name)
