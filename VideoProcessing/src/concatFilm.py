#import everything needed to edit video clips
from moviepy.editor import *

#define clips
clip1 = VideoFileClip("./data/testimage.mp4")
clip2 = VideoFileClip("./data/rotatevideo.mp4")

#create combined clip
result = concatenate_videoclips([clip1, clip2])

#write output video
result.write_videofile('./data/result.mp4')