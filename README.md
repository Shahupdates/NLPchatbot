# NLPchatbot

This code preprocesses input text by converting it to lowercase, tokenizing it, removing stopwords, and lemmatizing the words. It then transforms the input and corpus using a term frequency-inverse document frequency (tf-idf) vectorizer, and computes the cosine similarity between the input and corpus to determine the most similar response. If the similarity score is less than 0.5, it returns a default response. Otherwise, it returns the corresponding response from the corpus.
