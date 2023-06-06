import shutil
import sys

# Specify source file and destination file
source_file = 'final_video.mp4'
video_name = sys.argv[1] if len(sys.argv) > 1 else 'newvideo.mp4'
destination_file = f'Videos/{video_name}.mp4'

# Copy the file to new directory
shutil.copy(source_file, destination_file)
