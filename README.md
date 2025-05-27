## 🧠 Assignment: Build a Simple FAQ Chatbot in Python (NLP + GUI)
# 🎯 Goal
Create a simple, purpose-driven FAQ chatbot using Python.
It should respond to user questions based on similarity to predefined FAQ questions and answers.

# 🧰 Required Libraries
scikit-learn (for TF-IDF vectorization and similarity computation)

streamlit (for the user interface)

nltk (optional, if you want to handle more advanced preprocessing in English)

# 🗂 File Structure
chatbot.py: Contain all UI code
chatbot_logic.py: Contains all the logic code

# 🔧 Functions to Implement
load_faq_data()

Loads a predefined list of (question, answer) pairs

You can hardcode them or load them from a JSON file

get_most_similar_question(user_input, questions)

Converts input and questions into TF-IDF vectors

Returns the index of the most similar question

respond_to_input(user_input)

Uses get_most_similar_question to find the best match

Returns the corresponding answer or a default fallback

launch_chat_ui()

Uses tkinter to build a simple chat window

Allows users to type questions and see bot replies in real-time

# ✅ Additional Features (Optional)
Support both English 

Add a confidence threshold: if similarity < X, respond with “I don’t understand.”

# 🏁 Goal
When you run:
streamlit run chatbot.py
You should see a GUI chatbot window. You can type a question, and it will respond with the closest matching FAQ answer.

