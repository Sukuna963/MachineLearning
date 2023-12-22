#import everything needed to edit video clips
from moviepy.editor import *

#define clips
clip = VideoFileClip("./data/testimage.mp4")

#create combined clip
result = clips_array([[clip,clip],[clip,clip]])

#write output video
result.write_videofile("./data/arrayResult.mp4")