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
        self.window.resizable(True, True)  # Make window resizable

        self.create_widgets()

    def create_widgets(self):
        chat_history_label = ttk.Label(self.window, text="Chat History:")
        chat_history_label.grid(column=0, row=0, padx=10, pady=10, sticky='W')

        self.chat_history = ScrolledText(self.window, state='disabled')
        self.chat_history.grid(column=0, row=1, padx=10, pady=10, sticky='NSEW')

        user_input_label = ttk.Label(self.window, text="Your Message:")
        user_input_label.grid(column=0, row=2, padx=10, pady=10, sticky='W')

        self.user_input = ttk.Entry(self.window, width=40)
        self.user_input.grid(column=0, row=3, padx=10, pady=10, sticky='EW')

        send_button = ttk.Button(self.window, text="Send", command=self.process_user_input)
        send_button.grid(column=0, row=4, padx=10, pady=10, sticky='E')

        clear_button = ttk.Button(self.window, text="Clear", command=self.clear_chat_history)
        clear_button.grid(column=0, row=4, padx=10, pady=10, sticky='W')

        self.user_input.focus()
        self.user_input.bind('<Return>', lambda event: self.process_user_input())

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)  # Make chat history expand with window size

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

    def clear_chat_history(self):
        self.chat_history.configure(state='normal')
        self.chat_history.delete(1.0, tk.END)
        self.chat_history.configure(state='disabled')

    def run(self):
        self.window.mainloop()
