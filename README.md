# Zen AI Voice & Text Assistant

An intelligent personal desktop and voice assistant powered by local Ollama (`llama3`) and a Flask backend.

## 🚀 Features

- **Dual-Input Interface:** Seamlessly switch between speech recognition and text typing.
- **Auto-Submission:** Real-time speech recognition automatically triggers command execution when speaking stops.
- **Desktop App Controller:** Launch Windows apps and tools (Spotify, WhatsApp, VS Code, Notepad, Chrome, Explorer, Calculator, and more) natively.
- **Code Generation & Editor Integration:** Automatically writes code files, renders syntax-highlighted code with 1-click copy in the browser, and opens files directly in your desktop code editor.
- **PowerPoint Presentation Generator:** Create multi-slide presentations automatically using Python-pptx.
- **Text-to-Speech (TTS):** Audible voice feedback from Zen using the browser's speech synthesis engine.
- **Modern Glassmorphism UI:** Dark theme, fluid animations, audio equalizer waves, and responsive layouts.

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask, Flask-CORS, requests, python-pptx
- **AI Engine:** [Ollama](https://ollama.com/) running `llama3`
- **Frontend:** HTML5, CSS3 Glassmorphism, Web Speech API (SpeechRecognition + SpeechSynthesis)

## 📦 Setup & Running

1. **Start Ollama with Llama 3:**
   ```bash
   ollama run llama3
   ```

2. **Install Python dependencies:**
   ```bash
   pip install flask flask-cors requests python-pptx
   ```

3. **Run the assistant:**
   ```bash
   cd zen-backend
   python app.py
   ```

4. **Open in Browser:**
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).
