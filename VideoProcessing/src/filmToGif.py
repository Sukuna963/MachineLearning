#import everything needed to edit video clips
from moviepy.editor import *

#load video
clip = VideoFileClip('./data/video.mp4')

#getting only first 3 seconds
clip = clip.subclip(0, 3)

#convert to gif
clip.write_gif('./data/test.gif')