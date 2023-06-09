import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import langdetect
import spacy
from textblob import TextBlob
import requests

nltk.download('stopwords')
nltk.download('punkt')

class Chatbot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = stopwords.words('english')
        self.corpus = self.load_corpus('corpus.txt')
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)
        self.nlp = spacy.load('en_core_web_sm')
        self.ner_model = spacy.load('en_core_web_sm')
        self.context = []

    def load_corpus(self, file_path):
        with open(file_path, 'r') as file:
            corpus = [self.preprocess_input_text(line.strip()) for line in file]
        return corpus

    def preprocess_input_text(self, input_text):
        lang = langdetect.detect(input_text)
        
        if lang == 'en':
            input_text = input_text.lower()
            words = nltk.word_tokenize(input_text)
            words = [self.lemmatizer.lemmatize(word) for word in words if word not in self.stop_words]
            input_text = ' '.join(words)
        elif lang == 'fr':
            # French preprocessing
            ...
        elif lang == 'es':
            # Spanish preprocessing
            ...
        
        return input_text

    def recognize_intent(self, input_text):
        doc = self.nlp(input_text)
        intent = None

        for token in doc:
            if token.pos_ == 'VERB':
                intent = token.lemma_
                break

        return intent

    def extract_entities(self, input_text):
        doc = self.ner_model(input_text)
        entities = []

        for ent in doc.ents:
            entities.append((ent.text, ent.label_))

        return entities

    def update_context(self, user_query, chatbot_response):
        self.context.append((user_query, chatbot_response))

    def analyze_sentiment(self, input_text):
        blob = TextBlob(input_text)
        sentiment = blob.sentiment.polarity

        return sentiment

    def fetch_weather(self, location):
        # Use an appropriate weather API to fetch the weather data for the specified location
        response = requests.get('https://api.weather.com/...')
        weather_data = response.json()

        return weather_data

    def handle_weather_intent(self, input_text):
        # Extract location from input_text
        location = self.extract_location(input_text)

        if location:
            weather_data = self.fetch_weather(location)
            # Process weather data and generate a response
            response = self.generate_response_based_on_weather(weather_data)
        else:
            response = 'Please provide a valid location.'

        return response

    def get_response(self, input_text):
        input_text = self.preprocess_input_text(input_text)
        intent = self.recognize_intent(input_text)
        entities = self.extract_entities(input_text)
        sentiment = self.analyze_sentiment(input_text)

        if intent == 'order':
            response = self.handle_order_intent(input_text)
        elif intent == 'weather':
            response = self.handle_weather_intent(input_text)
        else:
            response = self.generate_default_response(sentiment)

        self.update_context(input_text, response)

        return response
