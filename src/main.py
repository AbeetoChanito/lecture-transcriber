from frame_reader import FrameReader
from video_reader import VideoReader
from transition_handler import TransitionHandler
import cv2

video_capture = cv2.VideoCapture("sampleVideo.mp4")
frame_reader = iter(FrameReader(video_capture, 5))
video_reader = iter(VideoReader(frame_reader))

transition_handler = TransitionHandler(video_reader)

print(transition_handler.get_transition_read_text())