from frame_reader import FrameReader
from easyocr import Reader # type: ignore[import-untyped]

class VideoReader:
    def __init__(self, frame_reader: FrameReader, lang_list=["en"]):
        self.__frame_reader = frame_reader
        self.__text_reader = Reader(lang_list)
        self.__last_text = None

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            frame = next(self.__frame_reader)
        
            processed_text = self.__text_reader.readtext(frame, detail=0)

            return_value = None
            if self.__last_text is not None and self.__last_text != processed_text:
                return_value = processed_text

            self.__last_text = processed_text

            if return_value is not None:
                return return_value