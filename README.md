# Le Petit Mépris — AI Virtual Assistant

Desktop virtual assistant for **Le Petit Mépris**, a fictional ultra-exclusive 3-star Michelin restaurant. Built with Python and Tkinter, it connects to Google's Gemini API to deliver condescending, passive-aggressive, and in-character answers based on custom restaurant policies.

---

## Features

- **Context Injection (In-Context Learning):** Delivers accurate menu and policy information loaded from `servicios.txt` via system instructions without fine-tuning or retraining.
- **Custom Persona:** Fully tuned to respond with an elitist, passive-aggressive tone fitting high-end culinary snobbery.
- **Responsive GUI:** Tkinter chat interface featuring auto-scroll, message categorization, and clean dark-mode visuals.
- **Non-blocking API Calls:** Background threading keeps the desktop UI responsive while waiting for Gemini API responses.
- **Environment Security:** Loads API keys securely from `.env` using `python-dotenv` to avoid credential leaks.
- **API Error Handling:** Intercepts runtime errors (such as transient `503 Service Unavailable` spikes) and displays themed warnings.

---

## Project Structure

```text
RA1_AI_Assistant/
├── .env                # Local API credentials (ignored by Git)
├── .gitignore          # Prevents tracking virtual environments & secrets
├── requirements.txt    # Python dependencies
├── servicios.txt       # Restaurant domain knowledge (menu, rules, hours)
└── gui_assistant.py    # Main Tkinter desktop client
```

---

## Requirements

- Python 3.10+
- A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/)

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd RA1_AI_Assistant
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root folder:
   ```env
   API_KEY=your_gemini_api_key_here
   ```

---

## Usage

Ensure your virtual environment is active, then launch the app:

```bash
python gui_assistant.py
```

Type any inquiry regarding dishes, reservation policies, or opening hours, and press **Enter** or click **Enviar**.
