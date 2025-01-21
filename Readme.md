
# S-412 - Personal AI
A Flask-based Personal AI integrated with the Groq API for chat interactions. This application is developed by Siddhartha412 and features the AI named **S-412**, a chill conversational assistant.

---

## Features
- Accepts user input via a web interface.
- Processes inputs using Groq API with the custom prompt format.
- Returns refined AI-generated responses.
- Easily customizable for additional functionality.

---

## Requirements
- Python 3.8 or higher

- Virtual environment (optional but recommended)

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment (Optional)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**
   Install the necessary packages using the provided `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Taking Groq Api**
    Take a api from
   [Groq Website](https://console.groq.com/keys)

   
5. **Set Up Environment Variables**
   Create a `.env` file in the project root and add your Groq API key:
   ```env
   GROQ_API_KEY=your-groq-api-key
   ```

---

## Usage

1. **Run the Application**
   ```bash
   python app.py
   ```

2. **Access the Web Interface**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Interact with S-412**
   - Enter your prompt in the input field and submit.
   - Just chill and chat

---

## Project Structure

```
├── app.py             # Main application file
├── templates/
│   └── index.html     # HTML template for the web interface
├── requirements.txt   # List of dependencies
├── .env               # Environment variables
├── README.md          # Project documentation
```

---

## Customization
You can modify the `groq_chat_completion` function in `app.py` to refine the AI's behavior or change the model used.

---

## Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!

---

## License
This project is licensed under the MIT License.

---

### Made with ❤️ of Siddhartha412
