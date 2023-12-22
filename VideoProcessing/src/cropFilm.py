#import everything needed to edit video clips
from moviepy.editor import *

#define clips
clip = VideoFileClip("./data/video.mp4")

#apply crop vfx
clip = clip.fx(vfx.crop, x1=550, x2=640, y1=200, y2=300)

#write output video
clip.write_videofile("./data/cropResult.mp4")