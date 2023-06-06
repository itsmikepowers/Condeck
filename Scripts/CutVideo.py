import random
from pydub.utils import mediainfo
from moviepy.editor import VideoFileClip, AudioFileClip

# Define constants
VIDEO_FILENAME = "./Assets/landscape.mp4"
AUDIO_FILENAME = "audio.mp3"
OUTPUT_FILENAME = "final_video.mp4"  # Output filename

def random_start(length, clip_length):
    """Return a random start time for the clip."""
    return random.uniform(0, length - clip_length)

def cut_clip(video_filename, audio_filename, start, clip_length, output_filename):
    """Cut clip and save to file."""
    end = start + clip_length

    # Load video and extract clip
    video = VideoFileClip(video_filename).subclip(start, end)

    # Load audio file
    audio = AudioFileClip(audio_filename)

    # Set the audio of the video clip
    video.set_audio(audio).write_videofile(output_filename, codec='libx264')

    print(f"Saved clip to {output_filename}")

def main():
    # Get the duration of the audio file
    audio_info = mediainfo(AUDIO_FILENAME)
    audio_length = float(audio_info['duration'])

    # Get the duration of the video file
    video_info = mediainfo(VIDEO_FILENAME)
    video_length = float(video_info['duration'])

    start_time = random_start(video_length, audio_length)
    cut_clip(VIDEO_FILENAME, AUDIO_FILENAME, start_time, audio_length, OUTPUT_FILENAME)

if __name__ == "__main__":
    main()
