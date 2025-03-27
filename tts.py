"""
Text-to-Speech, Speech-to-Text, and Audio Playback Utilities
------------------------------------------------------
This module handles the core audio operations for the avatar TTS app:
- Text-to-Speech (via ElevenLabs)
- Audio playback (via PyAudio)
- Speech-to-Text transcription (via Google Speech Recognition)
"""

import io
import wave
import pyaudio
import speech_recognition as sr
from pydub import AudioSegment
from elevenlabs import ElevenLabs

# Constants
AUDIO_FILE = "output.wav"
VOICE = "Rachel"

# Initialize ElevenLabs client
TTS_CLIENT = ElevenLabs(api_key="sk_e1753096cf230d8e384a50a2e0296e3e532a78ce168c728e")
def generate_audio(text: str, voice: str = VOICE) -> str:
    """
    Generate speech audio from text using ElevenLabs and export it as WAV.

    Args:
        text (str): Text to synthesize.
        voice (str): Voice model name.

    Returns:
        str: Path to the generated WAV audio file.
    """
    audio_stream = TTS_CLIENT.generate(
        text=text,
        voice=voice,
        model="eleven_monolingual_v1",
        stream=True
    )
    audio_bytes = b"".join(audio_stream)
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
    audio.export(AUDIO_FILE, format="wav")
    return AUDIO_FILE

def play_audio(audio_path: str) -> None:
    """
    Play a WAV audio file.

    Args:
        audio_path (str): Path to the WAV file.
    """
    chunk = 1024
    wf = wave.open(audio_path, 'rb')
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    pa.terminate()

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribe speech from an audio file using Google STT API.

    Args:
        audio_path (str): Path to the WAV file.

    Returns:
        str: Transcribed text.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return "Speech not understood."
    except sr.RequestError as e:
        return f"Request error: {e}"
