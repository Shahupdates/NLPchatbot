import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
nltk.download('punkt')

class Chatbot:
    def __init__(self):
        # Initialize lemmatizer
        self.lemmatizer = WordNetLemmatizer()

        # Initialize stopwords
        self.stop_words = stopwords.words('english')

        # Load corpus from a file
        self.corpus = self.load_corpus('corpus.txt')

        # Initialize vectorizer
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)

    def load_corpus(self, file_path):
        with open(file_path, 'r') as file:
            corpus = [self.preprocess_input_text(line.strip()) for line in file]
        return corpus

    def preprocess_input_text(self, input_text):
        # Convert to lowercase
        input_text = input_text.lower()

        # Tokenize text
        words = nltk.word_tokenize(input_text)

        # Remove stopwords and lemmatize words
        words = [self.lemmatizer.lemmatize(word) for word in words if word not in self.stop_words]

        # Join words back into a sentence
        input_text = ' '.join(words)

        return input_text

    def get_response(self, input_text):
        # Preprocess input text
        input_text = self.preprocess_input_text(input_text)

        # Transform input text
        input_tfidf = self.vectorizer.transform([input_text])

        # Compute cosine similarity between input and corpus
        similarity_scores = cosine_similarity(input_tfidf, self.tfidf_matrix)

        # Get index of highest similarity score
        max_index = similarity_scores.argmax()

        # If similarity score is less than 0.5, return default response
        if similarity_scores[0][max_index] < 0.5:
            return 'Sorry, I didn\'t understand that.'

        # Return corresponding response
        return self.corpus[max_index]

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

if __name__ == '__main__':
    chatbot = Chatbot()
    gui = ChatbotGUI(chatbot)
    gui.run()
