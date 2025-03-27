# Avatar TTS

A simplified Python application that integrates a pre-trained Text-to-Speech (TTS) model with facial animation to generate talking avatar videos using text input.

---

## Features

- ✅ Generate synthetic voice using ElevenLabs (pre-trained TTS)
- ✅ Upload generated audio to D-ID
- ✅ Create a realistic facial animation with a simple avatar
- ✅ Play audio locally & transcribe it back using Speech-to-Text
- ✅ Open final animated video automatically in browser
- ✅ Store interaction history for debugging/demo

---

## Objective

> Develop a simplified version where a synthetic voice is synchronized with basic facial animations using a simple avatar and text input only.

This was built for an interview assignment with the following evaluation criteria:
- Accuracy of speech-to-text and text-to-speech
- Realism of facial animations
- Overall user experience

---

## Tech Stack

- Python 3.11+
- [ElevenLabs API](https://www.elevenlabs.io/) (TTS)
- [D-ID API](https://www.d-id.com/) (Avatar Animation)
- PyAudio + Pydub (Audio Playback)
- SpeechRecognition (STT)

---

## Setup Instructions

1. **Clone the repo:**
```bash
git clone https://github.com/your-username/avatar-tts-
cd avatar-tts-
```

2. **Create virtual environment & install dependencies:**
```bash
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

3. **Set your API keys:**
Update `tts.py` and `d_id_api.py` with your ElevenLabs and D-ID API credentials.

4. **Run the App:**
```bash
python main.py
```
---
## Methodology

This application takes user text input, generates speech using ElevenLabs (TTS), then synchronizes it with a simple avatar using D-ID's API to produce a talking head video. The generated voice is also transcribed back using Google STT to demonstrate accuracy.

---

## File Structure

```
📁 avatar-tts-app
├── main.py         # Main application logic
├── tts.py          # TTS/STT and playback utilities
├── d_id_api.py     # D-ID avatar API integration
├── history.json    # Logs previous sessions
├── README.md       # Project documentation
├── requirements.txt # Dependency list
```

---

## Sample Output
A synthetic video where Rachel's voice is animated with synchronized lip movement:

[Click to Watch Live Demo](https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C113780342164315009464/tlk_EJ2-wYsHGX1Olq5CXNEBo/1743084117336.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1743170538&Signature=IkM4B0Rc1kh%2BKzD9F%2Bk15Movc40%3D)

---

## Credits
- [ElevenLabs](https://www.elevenlabs.io/)
- [D-ID](https://www.d-id.com/)
- Inspiration: Real-time avatar speech systems & mock interview assignment

---

## Contact
Built by **Ali Abdullah** — `ali.abdullah.222003@gmail.com`

Feel free to reach out for collaborations or feedback!

---

## License
MIT License
