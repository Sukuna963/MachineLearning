#import everything needed to edit video clips
from moviepy.editor import *

#define clips
clip = VideoFileClip('./data/video.mp4')

#speed up clip
clip = clip.fx(vfx.speedx, 4)

#write output video
clip.write_videofile('./data/speedvideo.mp4')