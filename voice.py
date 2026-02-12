import edge_tts
import asyncio

async def save_voice(text, filename="voice.mp3"):
    communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
    await communicate.save(filename)

def generate_voice(script):
    asyncio.run(save_voice(script))
