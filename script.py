import requests

def generate_script(topic):
    prompt = f"""
    Write a 5-second engaging YouTube script about {topic}.
    Only one sentence.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
