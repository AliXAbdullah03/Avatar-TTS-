"""
Main Application Logic for Avatar TTS App
----------------------------------------
This module drives the application by:
- Accepting user input
- Running TTS and STT processes
- Uploading audio
- Generating and opening the talking avatar video
"""

import os
import json
import webbrowser
from datetime import datetime
from tts import generate_audio, play_audio, transcribe_audio
from d_id_api import upload_audio, create_talking_video, poll_for_video

# Constants
AVATAR_ID = "video-9HkYjzJMTkqTPqXKgjpTr"
VOICE = "Rachel"
HISTORY_FILE = "history.json"

def save_to_history(text: str, video_url: str) -> None:
    """
    Save interaction history to a JSON file.

    Args:
        text (str): Original user input text.
        video_url (str): URL of the generated video.
    """
    history_entry = {
        "text": text,
        "voice": VOICE,
        "avatar": AVATAR_ID,
        "video_url": video_url,
        "timestamp": datetime.now().isoformat()
    }
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    history.append(history_entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def main() -> None:
    """
    Entry point of the application.
    Handles TTS, STT, audio upload, and video generation.
    """
    print("\n🤖 Welcome to the Real-Time Avatar TTS/STT App!\n")

    while True:
        text = input("📝 Enter text to speak (or 'q' to quit): ")
        if text.strip().lower() == 'q':
            print("👋 Exiting. Bye!")
            break

        print("\n🎙️ Generating audio...")
        audio_path = generate_audio(text, VOICE)

        print("🔊 Playing audio locally...")
        play_audio(audio_path)

        print("🧠 Transcribing audio (STT)...")
        transcription = transcribe_audio(audio_path)
        print(f"📝 Transcription: {transcription}")

        print("☁️ Uploading audio to D-ID...")
        audio_url = upload_audio(audio_path)

        print("🎭 Creating animated avatar video...")
        talk = create_talking_video(audio_url, AVATAR_ID)

        if talk and "id" in talk:
            print("⏳ Polling for video completion...")
            video_url = poll_for_video(talk["id"])
            if video_url:
                print(f"\n🎬 Video is ready! Opening: {video_url}\n")
                webbrowser.open(video_url)
                save_to_history(text, video_url)
        else:
            print("❌ Failed to generate avatar. Please check the avatar ID or your API plan.")

if __name__ == "__main__":
    main()