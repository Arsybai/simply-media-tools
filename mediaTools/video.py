import cv2
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import crop as crp

def crop(video_path, x, y, w, h, output_path='cropped.mp4'):
    input_file = video_path
    output_file = output_path
    video = VideoFileClip(input_file)
    cropped_video = video.fx(crp, x1=x, y1=y, x2=x+w, y2=y+h)
    cropped_video.write_videofile(output_file)
    video.close()
    cropped_video.close()

def extract_audio(video_path, output_path='extracted_audio.mp3'):
    input_file = video_path
    output_file = output_path
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    video.close()
    audio.close()

def trim(video_path, start, end, output_path='trimmed.mp4'):
    clip = VideoFileClip(video_path)
    start_time = start
    end_time = end
    trimmed_clip = clip.subclip(start_time, end_time)
    trimmed_clip.write_videofile(output_path)