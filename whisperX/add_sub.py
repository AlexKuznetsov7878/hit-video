import datetime
import textwrap
import pysrt
from moviepy import editor
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})  # replace with your path to convert

def wrap_text(text):
    wrapper = textwrap.TextWrapper(width=50)  # modify the width to adjust to your need
    word_list = wrapper.wrap(text)
    return '\n'.join(word_list)

def make_subtitle_clips(subs):
    subtitle_clips = []

    for sub in subs:
        start_time = datetime.datetime.combine(datetime.date.today(), sub.start.to_time())
        end_time = datetime.datetime.combine(datetime.date.today(), sub.end.to_time())
        duration = (end_time - start_time).total_seconds()
        start_time_seconds = (
                    start_time - datetime.datetime.combine(datetime.date.today(), datetime.time())).total_seconds()

        text = wrap_text(sub.text)  # wrap the text

        if text.strip():  # check if the text is not empty
            text_clip = editor.TextClip(text, font='Arial', fontsize=24, color='white')
            subtitle_clip = text_clip.set_duration(duration).set_start(start_time_seconds).set_position(('center', 'bottom'))
            subtitle_clips.append(subtitle_clip)

    return subtitle_clips

# Load your video and srt file
video = VideoFileClip('mob_meeting.mp4')
srt_file = 'mob_meeting.srt'

# Load the subtitles from the srt file
subs = pysrt.open(srt_file)
subtitle_clips = make_subtitle_clips(subs)

# Overlay the subtitles onto the video
video_with_subs = editor.CompositeVideoClip([video] + subtitle_clips)

# Write the result to a file
video_with_subs.write_videofile('mob_meeting_sub.mp4', codec='libx264')
