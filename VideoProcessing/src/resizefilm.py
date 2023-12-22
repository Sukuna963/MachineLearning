#import everything needed to edit video clips
from moviepy.editor import *

#define clips
clip = VideoFileClip("./data/testimage.mp4")

#apply resize video
clip = clip.fx(vfx.resize, width=400)

#write output video
clip.write_videofile("./data/resizevideo.mp4")