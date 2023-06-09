# NLP Chatbot
Chatbot is an advanced conversational agent built using Python. It utilizes natural language processing and machine learning techniques to understand user queries and provide appropriate responses. The chatbot supports multiple languages, recognizes user intents, performs named entity recognition, maintains conversation context, analyzes sentiment, and integrates with external APIs.

# Features
* Language Support: The chatbot supports multiple languages and applies language-specific preprocessing steps for better understanding.
* Intent Recognition: It recognizes the intention or purpose behind the user's input, allowing for customized handling of specific requests.
* Named Entity Recognition (NER): It identifies and extracts important entities from the user's query, such as names, locations, dates, etc.
* Contextual Conversation: The chatbot maintains conversation context to provide more coherent and relevant responses.
* Sentiment Analysis: It analyzes the sentiment of the user's input to generate appropriate responses based on the emotional tone.
* Integration with External APIs: The chatbot integrates with external APIs to fetch real-time data or perform specific tasks, such as retrieving weather information.

# Prerequisites
* Python 3.x
* nltk
* scikit-learn
* langdetect
* spacy
* textblob
* requests

# Installation
1. Clone the repository: ``` git clone https://github.com/shahupdates/nlpchatbot ```
2. Install the required packages: ``` pip install -r requirements.txt ```


# Usage
1. Obtain an API key from OpenWeatherMap (https://openweathermap.org/) to enable weather functionality. Replace 'YOUR_API_KEY_HERE' in main.py with your actual API key.
2. Define the corpus sentences in a text file named corpus.txt, with each sentence on a new line.
3. Run the program: ``` python main.py ```
4. The chatbot GUI window will appear. Enter your queries into the text entry field and press Enter or click the "Send" button to interact with the chatbot. The conversation will be displayed in the scrollable chat history area.


# Customization
* To customize the chatbot's behavior, you can modify the corpus sentences in the corpus.txt file.
* You can implement additional methods in the Chatbot class in chatbot.py to handle specific intents or provide custom functionality.
* Customize the additional methods in main.py according to your requirements, such as handling specific intents or generating default responses.
* Extend the functionality of the chatbot by adding more external API integrations or implementing additional natural language processing techniques.

# License
* This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgements
* The developers of the libraries used in this project: nltk, scikit-learn, langdetect, spacy, textblob, and requests.
