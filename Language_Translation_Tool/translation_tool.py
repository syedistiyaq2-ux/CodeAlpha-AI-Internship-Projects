import tkinter as tk
from tkinter import ttk, messagebox
import requests


def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    source = source_language.get()
    target = target_language.get()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    try:
        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": f"{source}|{target}"
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        translated = data["responseData"]["translatedText"]

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception:
        messagebox.showerror(
            "Error",
            "Translation failed. Please check your internet connection."
        )


window = tk.Tk()
window.title("Language Translation Tool")
window.geometry("650x500")

title = tk.Label(
    window,
    text="Language Translation Tool",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

language_frame = tk.Frame(window)
language_frame.pack(pady=5)

tk.Label(language_frame, text="From:").grid(row=0, column=0, padx=5)

source_language = ttk.Combobox(
    language_frame,
    values=["en", "hi", "te", "ur", "fr", "es", "de"],
    width=10
)
source_language.set("en")
source_language.grid(row=0, column=1, padx=5)

tk.Label(language_frame, text="To:").grid(row=0, column=2, padx=5)

target_language = ttk.Combobox(
    language_frame,
    values=["en", "hi", "te", "ur", "fr", "es", "de"],
    width=10
)
target_language.set("hi")
target_language.grid(row=0, column=3, padx=5)

tk.Label(
    window,
    text="Enter text:",
    font=("Arial", 12, "bold")
).pack(anchor="w", padx=30, pady=(15, 5))

input_text = tk.Text(window, height=6, width=70)
input_text.pack()

translate_button = tk.Button(
    window,
    text="Translate",
    command=translate_text,
    font=("Arial", 12, "bold")
)
translate_button.pack(pady=15)

tk.Label(
    window,
    text="Translated text:",
    font=("Arial", 12, "bold")
).pack(anchor="w", padx=30, pady=(5, 5))

output_text = tk.Text(window, height=6, width=70)
output_text.pack()

window.mainloop()