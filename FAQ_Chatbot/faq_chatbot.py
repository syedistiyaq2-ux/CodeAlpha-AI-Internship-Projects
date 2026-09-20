import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def preprocess_text(text):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    words = [
        word for word in words
        if word.isalnum() and word not in stop_words
    ]
    return " ".join(words)


faqs = [
    ("What is the internship duration?",
     "The internship duration depends on the program schedule."),

    ("How do I submit my project?",
     "You can submit your completed project using the internship submission form."),

    ("Where should I upload my project?",
     "You should upload your project source code to GitHub."),

    ("How can I get my certificate?",
     "You need to complete the required tasks and submit your work to receive the certificate."),

    ("What programming language can I use?",
     "You can use Python for this project."),

    ("How do I contact support?",
     "You can contact the internship support team through the official communication channel.")
]


questions = [preprocess_text(item[0]) for item in faqs]
answers = [item[1] for item in faqs]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


def get_answer():
    user_question = question_entry.get().strip()

    if not user_question:
        messagebox.showwarning("Warning", "Please enter a question.")
        return

    user_question = preprocess_text(user_question)
    user_vector = vectorizer.transform([user_question])

    similarity = cosine_similarity(user_vector, question_vectors)

    best_match = similarity.argmax()
    best_score = similarity[0][best_match]

    if best_score < 0.2:
        answer = "Sorry, I don't have an answer for that question."
    else:
        answer = answers[best_match]

    answer_label.config(text=answer)


window = tk.Tk()
window.title("FAQ Chatbot")
window.geometry("600x400")

title = tk.Label(
    window,
    text="FAQ Chatbot",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

question_label = tk.Label(
    window,
    text="Ask your question:",
    font=("Arial", 12)
)
question_label.pack()

question_entry = tk.Entry(window, width=60)
question_entry.pack(pady=10)

ask_button = tk.Button(
    window,
    text="Ask",
    command=get_answer,
    font=("Arial", 12, "bold")
)
ask_button.pack(pady=10)

answer_title = tk.Label(
    window,
    text="Answer:",
    font=("Arial", 12, "bold")
)
answer_title.pack(pady=(20, 5))

answer_label = tk.Label(
    window,
    text="",
    wraplength=500,
    font=("Arial", 11)
)
answer_label.pack(pady=5)

window.mainloop()