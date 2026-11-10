```markdown
# Le Petit Mépris — AI Virtual Assistant

A desktop virtual assistant for "Le Petit Mépris", a prestigious 3-star Michelin restaurant. Built with Python and Tkinter, it integrates Google's Gemini API to deliver in-character, condescending, and passive-aggressive answers to incoming dining inquiries.

---

## Features

- **Context-Aware Responses:** Injects custom policies and menu data (`servicios.txt`) via system instructions without retraining the model.
- **Graphical User Interface (GUI):** A clean Tkinter desktop chat window with an auto-scrolling message history.
- **Asynchronous Requests:** API calls run on a separate background thread to keep the GUI responsive.
- **Secure Key Storage:** Keeps the Gemini API key hidden using local environment variables (`.env`).
- **Error Handling:** Gracefully intercepts API errors (such as `503 Service Unavailable` spikes) directly in the UI.

---

## Project Structure

```text
RA1_AI_Assistant/
├── .env                # API key (not tracked in Git)
├── .gitignore          # Prevents sensitive files from being pushed
├── requirements.txt    # Python dependencies
├── servicios.txt       # Restaurant context (menu, rules, hours)
└── gui_assistant.py    # Main GUI application script

```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd RA1_AI_Assistant

```

### 2. Set up a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
API_KEY=your_google_gemini_api_key_here

```

---

## Running the Application

Make sure your virtual environment is active, then run:

```bash
python gui_assistant.py

```

```

```
