from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

class InterviewChatbot:
    def __init__(self, filepath):
        self.questions = self.load_questions(filepath)

    def load_questions(self, filepath):
        with open(filepath, 'r') as file:
            return json.load(file)

    def respond(self, user_input):
        user_input = user_input.lower()
        if user_input in self.questions:
            responses = self.questions[user_input]
            return random.choice(responses)  
        else:
            return "I'm sorry, I don't have a response to that question."

chatbot = InterviewChatbot('data.json')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    if user_input.strip():  # Check if the user input is not empty after stripping whitespace
        response = chatbot.respond(user_input)
        return response
    else:
        return "Please enter a question."

if __name__ == "__main__":
    app.run(debug=True)
