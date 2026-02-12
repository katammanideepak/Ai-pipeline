import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("PEXELS_API_KEY")

def fetch_clips(topic):
    url = f"https://api.pexels.com/videos/search?query={topic}&per_page=3"
    headers = {"Authorization": API_KEY}

    response = requests.get(url, headers=headers)
    data = response.json()

    clips = []

    for i, video in enumerate(data["videos"]):
        video_url = video["video_files"][0]["link"]
        video_data = requests.get(video_url).content

        filename = f"clip_{i}.mp4"
        with open(filename, "wb") as f:
            f.write(video_data)

        clips.append(filename)

    return clips
