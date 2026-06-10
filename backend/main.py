from fastapi import FastAPI
from mistralai import Mistral
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

app = FastAPI()

@app.post("/chat")
def chat(message: dict):
    response = client.chat.complete(
        model="mi stral-small-2503",
        messages=[
            {"role": "???", "content": message["message"]}
        ]
    )
    return {"response": response.choices[0].message.content}

