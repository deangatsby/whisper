import whisper
import moviepy.editor as mp
from moviepy.editor import VideoFileClip
import os

#Load OpeAI Whisper model
model = whisper.load_model("medium")

# Set video and audio paths
video_file = "E:/_VIDEO PROJECTS/_WEBINARS/Winning Sectors and Top-Rated Stocks During Rate Cuts_September 2024/Winning Sectors and Top-Rated Stocks During Rate Cuts.mp4"
desktop_dir = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop')
audio_file = os.path.join(desktop_dir, "extracted_audio.mp3")  

# Validate that the desktop directory exists
if os.path.isdir(desktop_dir):
    print(f"Desktop directory exists: {desktop_dir}")
else:
    print(f"Error: Desktop directory does not exist: {desktop_dir}")
    exit(1)

# Check if the audio file already exists (optional: only if you want to validate the file existence)
if os.path.isfile(audio_file):
    print(f"Audio file already exists: {audio_file}")
else:
    print(f"Audio file does not exist yet (this is expected if you're about to create it): {audio_file}")

# Extract audio from video
try:
    video = VideoFileClip(video_file)
    audio = video.audio
    # Specify the codec explicitly for MP3
    audio.write_audiofile(audio_file, codec='mp3')
    print(f"Audio extracted successfully and saved to {audio_file}")
except Exception as e:
    print(f"Error extracting audio: {e}")
    exit(1)

# Check if the audio file was created
if not os.path.exists(audio_file):
    print(f"Audio file was not created: {audio_file}")
    exit(1)


# Transcribe audio
try:
    result = model.transcribe(audio_file)
    print(result["text"])
except Exception as e:
    print(f"Error transcribing audio: {e}")
    exit(1)

