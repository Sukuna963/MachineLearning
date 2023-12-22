#import evything needed to edit video clips
from moviepy.editor import *

#create a color image
clip = ColorClip(size = (320, 200), color=[255,32,32])

#set duration of the video
clip = clip.set_duration(5)

#set the screen speed
clip.fps = 24

#save output
clip.write_videofile("./data/test.mp4")