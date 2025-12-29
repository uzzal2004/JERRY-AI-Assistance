# 🧠 jerry - Personal AI Assistant

A sophisticated AI assistant powered by Google Gemini API, built with Object-Oriented Programming principles and Streamlit.

## 📹 Demo Video

https://drive.google.com/file/d/1ryhgXE3w75s6Fc5YrlsHaHGU5uPn1wJE/view?usp=sharing

## ✨ Features

- 💬 Natural conversation with context memory
- 🎭 Multiple roles: General Assistant, Tutor, Coding Assistant, Career Helper
- 💾 Persistent conversation memory (JSON-based)
- 🎨 jerry-themed UI
- 🛡️ Robust error handling
- 🔒 Secure API key management

## 🏗️ Project Structure

```
jerry_assistant/
│
├── app.py                      # Streamlit UI
├── jerry/
│   ├── assistant.py           # Main jerry brain
│   ├── gemini_engine.py       # Gemini API handler
│   ├── prompt_controller.py   # System behavior & role
│   └── memory.py              # Conversation memory
├── config/
│   └── settings.py            # Environment & config
├── .env                        # API key (not in git)
├── .env.example               # Template for .env
├── requirements.txt
└── README.md
```

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/jerry-assistant.git
cd jerry-assistant
```

2. Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
```

5. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey) and add it to `.env`:

```
GEMINI_API_KEY=your_actual_api_key_here
```

## 💻 Usage

Run the application:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`
