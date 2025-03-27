"""
D-ID API Integration Module
-----------------------------
This module provides helper functions for:
- Uploading audio files to D-ID
- Creating talking avatar videos
- Polling D-ID servers until the video is ready
"""

import time
import requests
from requests.auth import HTTPBasicAuth

API_USERNAME = "YWxpLmFiZHVsbGFoLjIyMjAwM0BnbWFpbC5jb20"
API_PASSWORD = "t9J0H7sjPwJE4MRAh8RIa"

# Base URL for D-ID API
BASE_URL = "https://api.d-id.com"

def upload_audio(audio_path: str) -> str:
    """
    Upload audio file to D-ID and retrieve the audio URL.

    Args:
        audio_path (str): Local path to the audio file.

    Returns:
        str: Public URL of uploaded audio.
    """
    with open(audio_path, 'rb') as file:
        response = requests.post(
            f"{BASE_URL}/audios",
            auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
            files={"audio": file}
        )
    response_data = response.json()
    return response_data.get("url", "")

def create_talking_video(audio_url: str, avatar_id: str) -> dict:
    """
    Send request to create a talking video with a given avatar and audio.

    Args:
        audio_url (str): Public URL of uploaded audio.
        avatar_id (str): ID of the selected avatar.

    Returns:
        dict: Response JSON from D-ID API.
    """
    payload = {
        "source_id": avatar_id,
        "script": {
            "type": "audio",
            "audio_url": audio_url
        }
    }
    response = requests.post(
        f"{BASE_URL}/talks",
        auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD),
        json=payload
    )
    return response.json()

def poll_for_video(video_id: str) -> str:
    """
    Continuously poll the D-ID server until video is ready.

    Args:
        video_id (str): ID of the generated video.

    Returns:
        str: Public URL to the completed video, or empty string on failure.
    """
    poll_url = f"{BASE_URL}/talks/{video_id}"
    while True:
        time.sleep(2)
        response = requests.get(poll_url, auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))
        result = response.json()
        if result.get("status") == "done":
            return result.get("result_url", "")
        elif result.get("status") == "error":
            print("❌ Error from D-ID:", result.get("error"))
            return ""
