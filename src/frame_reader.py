import cv2

class FrameReader:
    def __init__(self, reader: cv2.VideoCapture, read_rate: float = 0):
        self.__reader = reader

        video_fps = reader.get(cv2.CAP_PROP_FPS)
        self.__read_rate = int(read_rate * video_fps)

    def __iter__(self):
        return self
    
    def __get_frame(self):
        ret, frame = self.__reader.read()

        if not ret:
            raise StopIteration
        
        return frame

    def __next__(self):        
        for _ in range(self.__read_rate - 1):
            _ = self.__get_frame()

        return self.__get_frame()
