from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# AI Name
AI_NAME = "S-412"

# Initialize Groq Client
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Set it in the .env file.")

client = Groq(api_key=GROQ_API_KEY)

# Simulated Groq Chat Completion
def groq_chat_completion(user_input):
    """
    Interact with the Groq API for chat completion with a refined prompt.
    """
    refined_prompt = f"You are {AI_NAME} who is developed by siddhartha412 and who cannot code and who is a chill guy. Here is the user prompt: {user_input}"
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": refined_prompt}],
            model="gemma2-9b-it",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Route: Home with Input Form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if not user_input:
            return jsonify(error="Input cannot be empty.")
        
        # Call Groq AI for chat completion
        response = groq_chat_completion(user_input)
        
        # Return the response as JSON
        return jsonify(response=response)
    
    return render_template("index.html", ai_name=AI_NAME)

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
