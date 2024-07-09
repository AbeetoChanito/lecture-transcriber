from os.path import splitext
from werkzeug.datastructures import FileStorage
from tempfile import NamedTemporaryFile
import cv2
import numpy as np

VIDEO_FILE_EXTENSIONS = ["mp4", "avi", "mov"]

class InvalidFileExtension(Exception):
    pass

class VideoNotOpening(Exception):
    pass

def is_video_ext(filename: str):
    _, ext = splitext(filename)
    ext = ext.lower()

    return ext, any(ext.lower().endswith(valid_ext) for valid_ext in VIDEO_FILE_EXTENSIONS)

def load_video(file: FileStorage):
    ext, valid = is_video_ext(file.filename)

    if not valid:
        raise InvalidFileExtension

    with NamedTemporaryFile(suffix=ext) as video_temp_file:
        video_temp_file.write(file.stream.read())

        video_capture = cv2.VideoCapture(video_temp_file.name)

        if not video_capture.isOpened():
            raise VideoNotOpening
            
    return video_capture