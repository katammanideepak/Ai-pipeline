from script import generate_script
from voice import generate_voice
from visuals import fetch_clips
from video import create_video

def run_pipeline(topic):
    print("Generating script...")
    script = generate_script(topic)

    print("Generating voice...")
    generate_voice(script)

    print("Fetching visuals...")
    clips = fetch_clips(topic)

    print("Creating final video...")
    create_video(clips, "voice.mp3")

    print("✅ Video created: final_video.mp4")

if __name__ == "__main__":
    topic = input("Enter video topic: ")
    run_pipeline(topic)

