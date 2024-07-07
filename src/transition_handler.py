from video_reader import VideoReader
from typing import Iterator

class TransitionHandler:
    def __init__(self, video_reader: VideoReader):
        self.__video_reader = video_reader

    def get_transition_read_text(self):
        transition_read_text = []

        for frame_text in self.__video_reader:
            if len(transition_read_text) != 0 and all(e in frame_text for e in transition_read_text[-1]):
                transition_read_text.pop()

            transition_read_text.append(frame_text)

        return transition_read_text