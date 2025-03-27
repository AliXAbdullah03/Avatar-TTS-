# Avatar TTS App

A simplified Python application that integrates a pre-trained Text-to-Speech (TTS) model with facial animation to generate talking avatar videos using text input.

---

## 🚀 Features

- ✅ Generate synthetic voice using ElevenLabs (pre-trained TTS)
- ✅ Upload generated audio to D-ID
- ✅ Create a realistic facial animation with a simple avatar
- ✅ Play audio locally & transcribe it back using Speech-to-Text
- ✅ Open final animated video automatically in browser
- ✅ Store interaction history for debugging/demo

---

## 🎯 Objective

> Develop a simplified version where a synthetic voice is synchronized with basic facial animations using a simple avatar and text input only.

This was built for an interview assignment with the following evaluation criteria:
- Accuracy of speech-to-text and text-to-speech
- Realism of facial animations
- Overall user experience

---

## 🧰 Tech Stack

- Python 3.11+
- [ElevenLabs API](https://www.elevenlabs.io/) (TTS)
- [D-ID API](https://www.d-id.com/) (Avatar Animation)
- PyAudio + Pydub (Audio Playback)
- SpeechRecognition (STT)

---

## 🛠️ Setup Instructions

1. **Clone the repo:**
```bash
git clone https://github.com/your-username/avatar-tts-app
cd avatar-tts-app
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

## 📂 File Structure

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

## 📸 Sample Output
A synthetic video where Rachel's voice is animated with synchronized lip movement:

[![Watch on D-ID](https://img.shields.io/badge/Click%20to%20Preview-Video-blue)](https://your-video-link.com)

---

## 🤝 Credits
- [ElevenLabs](https://www.elevenlabs.io/)
- [D-ID](https://www.d-id.com/)
- Inspiration: Real-time avatar speech systems & mock interview assignment

---

## 📬 Contact
Built by **Ali Abdullah** — `ali.abdullah.222003@gmail.com`

Feel free to reach out for collaborations or feedback!

---

## 📄 License
MIT License (if open-sourced)
