from frame_reader import FrameReader
from easyocr import Reader
from cv2 import VideoCapture
from transition_handler import handle_transitions

reader = Reader(lang_list=["en"])

class VideoReader:
    def __init__(self, frame_reader: FrameReader):
        self.__frame_reader = frame_reader
        self.__last_text = None

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            frame = next(self.__frame_reader)
            processed_text = reader.readtext(frame, detail=0)

            if self.__last_text is not None and self.__last_text != processed_text:
                self.__last_text = processed_text
                return processed_text

            self.__last_text = processed_text

def transcribe_video(capture: VideoCapture, read_rate: float = 5):
    frame_reader = iter(FrameReader(capture, read_rate))
    video_reader = iter(VideoReader(frame_reader))

    return "\n".join([
        " ".join(phrase)
        for phrase in handle_transitions(video_reader)
    ])