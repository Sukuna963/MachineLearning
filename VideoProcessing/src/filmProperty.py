#import evything needed to edit video clips
from moviepy.editor import *

#open movie
clip = VideoFileClip("./data/test.mp4")

#show width
print(clip.w)

#show height
print(clip.h)

#size
print(clip.size)

#duration
print(clip.duration)

#frame rate
print(clip.fps)