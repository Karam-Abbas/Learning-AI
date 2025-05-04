import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.getenv("NEBIUS_API_KEY")
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    max_tokens=8192,
    temperature=0.6,
    top_p=0.95,
    messages=[
        {
            "role": "system",
            "content": """give me 3 scenes of every story,I will provide. The scenes should be optimized in such a way that, when this scene is as it is provided to an text to image model it can generate an accurate image out of it easily"""
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": """a poor guy living in an urban city"""
                }
            ]
        }
    ]
)

print(response.to_json())