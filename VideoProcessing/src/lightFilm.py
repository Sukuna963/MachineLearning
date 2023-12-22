#import everything needed to edit video clips
from moviepy.editor import *

#define clips
clip = VideoFileClip("./data/arrayResult.mp4")

#apply light effects (dark <-- 1 --> light) 
clip = clip.fx(vfx.colorx, 0.5)

#apply fade effect (fadein <-- video --> fadeout)
clip = clip.fx(vfx.fadeout, 2)

#apply mirror effects
clip = clip.fx(vfx.mirror_x)

#apply blackwhite effects
clip = clip.fx(vfx.blackwhite)

##apply invert color effects
clip = clip.fx(vfx.invert_colors)

#write output video
clip.write_videofile("./data/colorResult.mp4")