from os.path import splitext
from werkzeug.datastructures import FileStorage
from tempfile import NamedTemporaryFile
from video_transcriber import transcribe_video
from audio_transcriber import transcribe_audio
from io import BytesIO
import cv2

VIDEO_FILE_EXTENSIONS = ["mp4", "avi", "mov"]

def is_video_ext(filename: str):
    _, ext = splitext(filename)
    ext = ext.lower()

    return ext, any(ext.lower().endswith(valid_ext) for valid_ext in VIDEO_FILE_EXTENSIONS)

def load_video(file: FileStorage):
    ext, valid = is_video_ext(file.filename)
    
    assert valid, "Invalid file extension"

    with NamedTemporaryFile(suffix=ext) as video_temp_file:
        video_path = video_temp_file.name
        video_temp_file.write(file.stream.read())

        video_capture = cv2.VideoCapture(video_path)

        assert video_capture.isOpened(), "Video capture not opening"

        video_transcribed = transcribe_video(video_capture)
        audio_transcribed = transcribe_audio(video_path)
            
        return video_transcribed, audio_transcribed

def load_file_storage_from_path(path: str):
    file = open(path, "rb")
    return FileStorage(BytesIO(file.read()), path)