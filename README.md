# Avatar TTS App

A simplified Python application that integrates a pre-trained Text-to-Speech (TTS) model with facial animation to generate talking avatar videos using text input.

🚀 Features

✅ Generate synthetic voice using ElevenLabs (pre-trained TTS)

✅ Upload generated audio to D-ID

✅ Create a realistic facial animation with a simple avatar

✅ Play audio locally & transcribe it back using Speech-to-Text

✅ Open final animated video automatically in browser

✅ Store interaction history for debugging/demo

🎯 Objective

Develop a simplified version where a synthetic voice is synchronized with basic facial animations using a simple avatar and text input only.

This was built for an interview assignment with the following evaluation criteria:

Accuracy of speech-to-text and text-to-speech

Realism of facial animations

Overall user experience

🧰 Tech Stack

Python 3.11+

ElevenLabs API (TTS)

D-ID API (Avatar Animation)

PyAudio + Pydub (Audio Playback)

SpeechRecognition (STT)

🛠️ Setup Instructions

Clone the repo:

git clone https://github.com/your-username/avatar-tts-app
cd avatar-tts-app

Create virtual environment & install dependencies:

python -m venv venv
# venv\Scripts\activate     # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

Set your API keys:
Update tts.py and d_id_api.py with your ElevenLabs and D-ID API credentials.

Run the App:

python main.py

📂 File Structure

├── main.py              # Main application logic
├── tts.py               # TTS/STT and playback utilities
├── d_id_api.py          # D-ID avatar API integration
├── history.json         # Logs previous sessions
├── README.md            # This file

📸 Sample Output

A synthetic video where Rachel's voice is animated with synchronized lip movement:



🤝 Credits

ElevenLabs

D-ID

Inspiration: Real-time avatar speech systems & mock interview assignment

📬 Contact

Built by Ali Abdullah — ali.abdullah.222003@gmail.com

Feel free to reach out for collaborations or feedback!

📄 License

MIT License
