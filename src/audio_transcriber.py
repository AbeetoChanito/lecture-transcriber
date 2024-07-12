from moviepy.editor import VideoFileClip
from speech_recognition import Recognizer, AudioFile
from tempfile import NamedTemporaryFile

recognizer = Recognizer()

AUDIO_FILE_EXTENSION = ".wav"
VALID_RECOGNIZER_TYPES = ["sphinx", "google"]

def extract_video(video_path: str, output_path: str):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path, codec="pcm_s16le", logger=None)

def recognize_speech(audio_file: AudioFile, recognizer_type="sphinx"):
    if recognizer_type not in VALID_RECOGNIZER_TYPES:
        raise Exception("invalid recognizer type")

    with audio_file as source:
        audio = recognizer.record(source)

        return eval(f"recognizer.recognize_{recognizer_type}(audio)")

def transcribe_audio(video_path: str):
    with NamedTemporaryFile(suffix=AUDIO_FILE_EXTENSION) as audio_temp_file:
        output_path = audio_temp_file.name
        
        extract_video(video_path, output_path)
        audio_file = AudioFile(output_path)

        return recognize_speech(audio_file)