from moviepy.editor import VideoFileClip
from speech_recognition import Recognizer, AudioFile
from tempfile import NamedTemporaryFile

recognizer = Recognizer()

AUDIO_FILE_EXTENSION = ".wav"

def extract_video(video_path: str, output_path: str):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path, codec="pcm_s16le")

def recognize_speech(audio_file: AudioFile):
    with audio_file as source:
        audio = recognizer.record(source)

        return recognizer.recognize_google(audio)

def extract_from_video(video_path: str):
    with NamedTemporaryFile(suffix=AUDIO_FILE_EXTENSION) as audio_temp_file:
        output_path = audio_temp_file.name
        
        extract_video(video_path, output_path)
        audio_file = AudioFile(output_path)

        return recognize_speech(audio_file)
    
print(extract_from_video("sampleVideo.mp4"))