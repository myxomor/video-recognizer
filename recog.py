from easyocr import Reader
import cv2
from datetime import timedelta
import cv2
import numpy as np
import os

SAVING_FRAMES_PER_SECOND = 0.1

def get_saving_frames_durations(cap, saving_fps):
    s = []
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s

langs = ['en', 'ru']
print("Languages: {}".format(langs))
reader = Reader(langs, 0)


cap = cv2.VideoCapture("video_file.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
count = 0
while True:

	is_read, frame = cap.read()
	if not is_read:
		break
	frame_duration = count / fps
	try:
		closest_duration = saving_frames_durations[0]
	except IndexError:
		break
	if frame_duration >= closest_duration:
		print(f'Kadr {count}')
		reader = Reader(langs, 0)
		results = reader.readtext(frame)
		for (bbox, text, prob) in results:
			print("{:.4f}: {}".format(prob, text))
		try:
			saving_frames_durations.pop(0)
		except IndexError:
			pass
	count += 1
