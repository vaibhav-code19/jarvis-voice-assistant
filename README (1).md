
# # Jarvis – Voice Assistant using Python + Groq AI

Jarvis is a voice-controlled virtual assistant built in Python that responds to your commands, plays music, opens websites, fetches news, and answers questions using LLaMA-3 from Groq. It mimics real-world assistants like Alexa, Siri, and Google Assistant.

Ideal for beginners, hobbyists, or anyone exploring AI + voice tech.



## Features

- Voice wake word detection (“Jarvis”)
- AI-powered replies using LLaMA-3 via Groq API
- Top headlines from NewsAPI
- Opens websites like Google, YouTube, LinkedIn, etc.
- Custom music library support
- Uses `.env` for API key security


## Installation

1. Clone the repository:
git clone https://github.com/yourusername/jarvis-assistant.git

2. Navigate into the folder:
cd jarvis-assistant

3. Install dependencies:
pip install -r requirements.txt

4. Create a `.env` file and add your API keys:
GROQ_API_KEY=your_groq_api_key
NEWS_API_KEY=your_newsapi_key

5. Run it:


    
## Usage/Examples

Speak the word “Jarvis” to activate the assistant. Then try commands like:

- "Open Google"
- "Play More than Friends"
- "Read the news"
- "What's the capital of Germany?"

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

Create a `.env` file and add:
`GROQ_API_KEY=your_groq_api_key`
`NEWS_API_KEY=your_newsapi_key`

✅ These keys are kept private and not pushed to GitHub thanks to `.gitignore`

## Tech Stack 

- Python 3.10+
- SpeechRecognition
- pyttsx3
- Groq API (LLaMA-3)
- NewsAPI
- dotenv
- Webbrowser

## API Reference

### Groq API (LLaMA-3)

#### Get all items

Used for generating smart replies to user queries.

- Endpoint: `https://api.groq.com/openai/v1`
- Model: `llama3-8b-8192` or `llama3-70b-8192`
- Library: `openai` (used with custom client)

### NewsAPI
Used to fetch the latest headlines.

- Endpoint: `https://newsapi.org/v2/top-headlines`
- Parameters: `q`, `sortBy`, `pageSize`, `language`, `apiKey`

## Author/Contact

## Author

Built with ❤️ by [Vaibhav Verma](https://x.com/vaibhavv190)

📫 Email: vaibhav1909verma@gmail.com

> Always open to feedback, collaborations, and tech conversations.
