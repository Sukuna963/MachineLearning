#import evything needed to edit video clips
from moviepy.editor import *

#load video and edit it
video = VideoFileClip('./data/testimage.mp4').rotate(90)

#write video
video.write_videofile("./data/rotatevideo.mp4")