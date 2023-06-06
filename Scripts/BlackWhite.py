from moviepy.editor import VideoFileClip
from moviepy.video import fx
import os

def convert_to_bw(video_path, output_path):
    clip = VideoFileClip(video_path)

    bw_clip = clip.fx(fx.all.blackwhite)

    bw_clip.write_videofile(output_path, codec='libx264')

convert_to_bw("final_video.mp4", "final_video_bw.mp4")

def rename_video_file(old_name, new_name):
    try:
        os.replace(old_name, new_name)
        print("Video file renamed successfully.")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Specify the old and new file names
old_file_name = "final_video_bw.mp4"
new_file_name = "final_video.mp4"

# Call the rename_video_file function
rename_video_file(old_file_name, new_file_name)
