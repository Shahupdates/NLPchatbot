import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# download stopwords
nltk.download('stopwords')

# initialize stopwords
stop_words = stopwords.words('english')

# preprocess input text
def preprocess_input_text(input_text):
    # convert to lowercase
    input_text = input_text.lower()
    
    # tokenize text
    words = nltk.word_tokenize(input_text)
    
    # remove stopwords and lemmatize words
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    # join words back into sentence
    input_text = ' '.join(words)
    
    return input_text

# initialize corpus
corpus = [
    'Hi there, how can I help you today?',
    'What would you like to know?',
    'I can help you with that.',
    'Sorry, I didn\'t understand that.',
    'Please provide more information.',
    'Thank you for your inquiry.'
]

# preprocess corpus
corpus = [preprocess_input_text(text) for text in corpus]

# initialize vectorizer
vectorizer = TfidfVectorizer()

# fit and transform corpus
tfidf_matrix = vectorizer.fit_transform(corpus)

# initialize chatbot
def chatbot(input_text):
    # preprocess input text
    input_text = preprocess_input_text(input_text)
    
    # transform input text
    input_tfidf = vectorizer.transform([input_text])
    
    # compute cosine similarity between input and corpus
    similarity_scores = cosine_similarity(input_tfidf, tfidf_matrix)
    
    # get index of highest similarity score
    max_index = similarity_scores.argmax()
    
    # if similarity score is less than 0.5, return default response
    if similarity_scores[0][max_index] < 0.5:
        return 'Sorry, I didn\'t understand that.'
    
    # return corresponding response
    return corpus[max_index]

# test chatbot
input_text = 'Can you help me with my order?'
print(chatbot(input_text)) # output: 'I can help you with that.'
