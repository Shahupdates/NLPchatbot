import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from chatbot import Chatbot

class ChatbotGUI:
    def __init__(self, chatbot):
        self.chatbot = chatbot

        self.window = tk.Tk()
        self.window.title("Chatbot")
        self.window.geometry("400x500")

        self.create_widgets()

    def create_widgets(self):
        self.chat_history = ScrolledText(self.window, state='disabled')
        self.chat_history.pack(expand=True, fill='both')

        self.user_input = ttk.Entry(self.window, width=40)
        self.user_input.pack(pady=10)

        send_button = ttk.Button(self.window, text="Send", command=self.process_user_input)
        send_button.pack()

        self.user_input.focus()
        self.user_input.bind('<Return>', lambda event: self.process_user_input())

    def process_user_input(self):
        user_query = self.user_input.get()
        self.user_input.delete(0, tk.END)

        response = self.chatbot.get_response(user_query)

        self.display_message(user_query, is_user=True)
        self.display_message(response, is_user=False)

    def display_message(self, message, is_user):
        self.chat_history.configure(state='normal')
        if is_user:
            self.chat_history.insert(tk.END, "You: " + message + "\n")
        else:
            self.chat_history.insert(tk.END, "Chatbot: " + message + "\n")
        self.chat_history.configure(state='disabled')
        self.chat_history.see(tk.END)

    def run(self):
        self.window.mainloop()
