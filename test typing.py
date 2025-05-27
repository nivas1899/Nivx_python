import tkinter as tk
from tkinter import messagebox
import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an easy to learn programming language.",
    "Typing speed depends on accuracy and practice.",
    "Artificial Intelligence is changing the world.",
    "Tkinter makes it easy to build GUIs in Python."
]

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        self.sentence = random.choice(sentences)
        self.start_time = None

        self.label_title = tk.Label(root, text="Typing Speed Test", font=("Arial", 24, "bold"))
        self.label_title.pack(pady=10)

        self.label_sentence = tk.Label(root, text=self.sentence, font=("Arial", 14), wraplength=600)
        self.label_sentence.pack(pady=20)

        self.text_input = tk.Text(root, height=5, width=70, font=("Arial", 12))
        self.text_input.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start_test, bg="green", fg="white", width=10)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.end_test, bg="red", fg="white", width=10)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

    def start_test(self):
        self.text_input.delete("1.0", tk.END)
        self.sentence = random.choice(sentences)
        self.label_sentence.config(text=self.sentence)
        self.start_time = time.time()
        self.result_label.config(text="")
        self.text_input.focus()

    def end_test(self):
        if self.start_time is None:
            messagebox.showwarning("Warning", "Click Start to begin the test!")
            return

        end_time = time.time()
        time_taken = end_time - self.start_time
        typed_text = self.text_input.get("1.0", tk.END).strip()

        word_count = len(typed_text.split())
        speed_wpm = word_count / (time_taken / 60)

        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(self.sentence) and c == self.sentence[i])
        accuracy = (correct_chars / len(self.sentence)) * 100

        self.result_label.config(
            text=f"Time: {time_taken:.2f}s | Speed: {speed_wpm:.2f} WPM | Accuracy: {accuracy:.2f}%"
        )
        self.start_time = None

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
