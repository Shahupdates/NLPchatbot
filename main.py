from chatbot import Chatbot
from chatbot_gui import ChatbotGUI

if __name__ == '__main__':
    chatbot = Chatbot()
    gui = ChatbotGUI(chatbot)
    gui.run()
