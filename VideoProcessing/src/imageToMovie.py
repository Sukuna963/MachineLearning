#import everything needed to edit video clips
from moviepy.editor import *

#create a image sequence
clip = ImageSequenceClip(['./data/1.jpg', './data/2.jpg'], fps = 1)

#save output
clip.write_videofile("./data/testimage.mp4")