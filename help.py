import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from datetime import datetime

class HelpDeskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Desk Assistant")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        self.root.wm_iconbitmap("front.ico")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Arial", 11))
        self.style.configure("TLabel", font=("Arial", 11))
        self.style.configure("TEntry", font=("Arial", 11))

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Welcome to Help Desk", font=("Arial", 16, "bold")).pack(pady=10)

        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 11), height=20, state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        input_frame = ttk.Frame(self.root)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        self.user_input = ttk.Entry(input_frame)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)

        send_button = ttk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        message = self.user_input.get().strip()
        if not message:
            return

        self.display_message("You", message)
        self.user_input.delete(0, tk.END)

        response = self.get_bot_response(message)
        self.display_message("Bot", response)

    def display_message(self, sender, message):
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender} ({timestamp}): {message}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def get_bot_response(self, message):
        message = message.lower()

        if "hello" in message or "hi" in message:
            return "Hello! How can I help you today?"
        elif "issue" in message or "problem" in message:
            return "Could you please describe the issue in more detail?"
        elif "issue" in message or "error" in message:
            return "Could you please describe the issue in more detail?"
        elif "issue" in message or "error" in message:
            return "Could you please describe the issue in more detail?"
        elif "thanks" in message or "thank you" in message:
            return "You're welcome! Let me know if you need anything else."
        elif "bye" in message:
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I didn't understand that. Can you rephrase it?"

if __name__ == "__main__":
    root = tk.Tk()
    app = HelpDeskApp(root)
    root.mainloop()
