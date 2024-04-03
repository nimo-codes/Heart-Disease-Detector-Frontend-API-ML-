from pydantic import BaseModel
from typing import List
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os

class TextEntry(BaseModel):
    text: str
    duration: int = 5

def animate_text_move(text_entries: List[TextEntry], vid_pth, final_pth):
    animated_clips = []

    for entry in text_entries:
        text = entry.text
        duration = entry.duration
        txt_clip = TextClip(text, fontsize=50, color='white')
        txt_clip = txt_clip.set_position(('center', 'top')).set_duration(duration).set_start(0)
        animated_clips.append(txt_clip)

    video_clip = VideoFileClip(vid_pth)
    final_clip = CompositeVideoClip([video_clip] + animated_clips)
    final_clip.write_videofile(final_pth, codec='libx264')
    return final_pth



if __name__ == "__main__":
    vid_pth = input("Enter the path of the video: ")
    final_pth = input("Enter the Output path of the Generated video: ")
    txt = input("Enter the text to be displayed or Overlayed: ")
    dur = int(input("Enter the time(seconds) for the text to appear: "))
    text_entries = [TextEntry(text="Hello", duration=5), TextEntry(text= txt, duration=dur)]
    out_vid_pth = animate_text_move(text_entries, vid_pth, final_pth)
    print("Output video saved at:", out_vid_pth)
