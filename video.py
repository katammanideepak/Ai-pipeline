import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, afx

def create_video(clips, audio_path):
    if not os.path.exists(audio_path) or os.path.getsize(audio_path) == 0:
        print(f"❌ Error: Audio file {audio_path} is missing or empty!")
        return

    # Load audio
    audio = AudioFileClip(audio_path)
    
    # Load video clips without audio
    video_clips = [VideoFileClip(c).without_audio() for c in clips]

    # Combine all clips
    combined = concatenate_videoclips(video_clips, method="compose")

    # Loop audio only if shorter than video
    if audio.duration < combined.duration:
        audio = afx.audio_loop(audio, duration=combined.duration)

    # Attach audio
    final_video = combined.set_audio(audio)

    # Export video
    final_video.write_videofile(
        "final_video.mp4",
        codec="libx264",
        audio_codec="aac",
        fps=video_clips[0].fps,
        temp_audiofile="temp-audio.m4a",
        remove_temp=True
    )

    print(f"✅ Final video created successfully ({combined.duration:.2f} sec) with audio.")
