from chatbot import Chatbot
from chatbot_gui import ChatbotGUI

if __name__ == '__main__':
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your actual API key
    chatbot = Chatbot(api_key)
    gui = ChatbotGUI(chatbot)

    # Additional methods
    def handle_order_intent(chatbot, input_text):
        # Handle order-related queries
        ...

    def generate_default_response(chatbot, sentiment):
        # Generate default response based on sentiment
        ...

    # Add the additional methods to the chatbot object
    chatbot.handle_order_intent = handle_order_intent
    chatbot.generate_default_response = generate_default_response

    gui.run()
