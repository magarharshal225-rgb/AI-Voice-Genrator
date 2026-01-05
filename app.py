from fastapi import FastAPI, Query
from TTS.api import TTS
import uuid
import os

app = FastAPI(title="AI Voice Generator")

# Load multilingual model (Hindi + English)
tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/your_tts",
    progress_bar=False,
    gpu=False  # set True if GPU available
)

# Create output folder
os.makedirs("outputs", exist_ok=True)

@app.get("/")
def home():
    return {"status": "AI Voice Generator is running"}

@app.post("/generate")
def generate_voice(
    text: str = Query(..., description="Text to convert into speech"),
    language: str = Query("hi", description="hi for Hindi, en for English")
):
    file_name = f"outputs/voice_{uuid.uuid4()}.wav"

    tts.tts_to_file(
        text=text,
        file_path=file_name,
        speaker_wav=None,   # later add your voice sample
        language=language
    )

    return {
        "message": "Voice generated successfully",
        "audio_file": file_name
    }
