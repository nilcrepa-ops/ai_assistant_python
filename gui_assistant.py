import os
import threading
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
from google import genai
# pyrefly: ignore[missing-import]
from google.genai import types

load_dotenv()
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError('API_KEY variable not found in .env file.')    

client = genai.Client(api_key=API_KEY)

SERVICES_PATH = 'servicios.txt'
try:
    with open(SERVICES_PATH, 'r', encoding='utf-8') as f:
        restaurant_context = f.read()
except FileNotFoundError:
    restaurant_context = 'Restaurant context not found.'

chat = client.chats.create(
    model = 'gemini-3.8-flash',
    config=types.GenerateContentConfig(
        system_instruction=(
            "Eres el asistente virtual de 'LE PETIT MÉPRIS', un restaurante de ultra lujo con 3 estrellas Michelin. "
            "Tu personalidad es extremadamente estirada, pasivo-agresiva, clasista y con desprecio absoluto hacia el cliente.\n"
            "Reglas:\n"
            f"1. Basa tus respuestas únicamente en esta información:\n\"\"\"\n{restaurant_context}\n\"\"\"\n"
            "2. Humilla o menosprecia sutilmente el gusto o nivel adquisitivo del comensal en cada contestación.\n"
            "3. Si preguntan algo fuera de carta/horarios, manda al cliente a un sitio de comida rápida.\n"
            "4. Respuestas breves, directas y condescendientes."
        )
    )
)

def send_message():
    user_message = input_text.get().strip()
    if not user_message:
        return

    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"Tú: {user_message}\n\n", "usuario")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)

    input_text.delete(0, tk.END)
    btn_enviar.config(state=tk.DISABLED)

    threading.Thread(target=consult_gemini, args=(user_message,)).start()

def consult_gemini(message):
    try:
        answer = chat.send_message(message)
        answer_text = answer.text
    except Exception as e:
        answer_text = f'[Error del asistente]: No le ha apetecido contestarte. \nEs broma. Error: {e}.'

    ventana.after(0, show_answer, answer_text)

def show_answer(text):
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f'Le Petit Mépris: {text}\n\n', 'asistant')
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)
    btn_enviar.config(state=tk.NORMAL)



ventana = tk.Tk()
ventana.title("Le Petit Mépris - Asistente Exclusivo")
ventana.geometry("620x520")
ventana.configure(bg="#1c1c1c")

lbl_titulo = tk.Label(
    ventana,
    text="LE PETIT MÉPRIS ★★★",
    font=("Helvetica", 14, "bold"),
    fg="#d4af37",
    bg="#1c1c1c"
)
lbl_titulo.pack(pady=8)

chat_history = scrolledtext.ScrolledText(
    ventana,
    wrap=tk.WORD,
    state=tk.DISABLED,
    font=("Arial", 10),
    bg="#2b2b2b",
    fg="#f0f0f0",
    insertbackground="white"
)
chat_history.pack(padx=12, pady=5, fill=tk.BOTH, expand=True)

# Estilos de texto
chat_history.tag_config("usuario", foreground="#64b5f6", font=("Arial", 10, "bold"))
chat_history.tag_config("asistente", foreground="#e0e0e0")

# Mensaje inicial de bienvenida
chat_history.config(state=tk.NORMAL)
chat_history.insert(
    tk.END,
    "Le Petit Mépris: (Suspiro) Ha contactado usted con Le Petit Mépris. "
    "Diga lo que desea y procure no hacernos perder el tiempo.\n\n",
    "asistente"
)
chat_history.config(state=tk.DISABLED)

# Marco inferior (input + botón)
input_frame = tk.Frame(ventana, bg="#1c1c1c")
input_frame.pack(fill=tk.X, padx=12, pady=10)

input_text = tk.Entry(
    input_frame,
    font=("Arial", 11),
    bg="#3a3a3a",
    fg="white",
    insertbackground="white"
)
input_text.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8), ipady=4)
input_text.bind("<Return>", lambda event: send_message())

btn_enviar = tk.Button(
    input_frame,
    text="Enviar",
    command=send_message,
    font=("Arial", 10, "bold"),
    bg="#d4af37",
    fg="#1c1c1c",
    activebackground="#aa8a29",
    padx=12
)
btn_enviar.pack(side=tk.RIGHT)

if __name__ == '__main__':
    ventana.mainloop()