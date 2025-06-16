import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary 
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

# pip install pocketsphinx (optional or not needed if using recognize_google)
# pip install requests
# pip install openai
# pip install dotenv


# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
load_dotenv()

# New API key
newsapi = os.getenv("NEWS_API_KEY")

# Tecxt-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Process AI response from Groq AI
def aiProcess(command):
    client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
    )

    completion = client.chat.completions.create(
    model="llama3-8b-8192",  # or llama3-70b-8192
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa, Siri and GoogleCloud. Give short to brief responses"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

# Handle common commands
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open x" in c.lower():
        webbrowser.open("https://x.com/vaibhavv190")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        if song in musiclibrary.music:
             link = musiclibrary.music[song]
             webbrowser.open(link)
        else:
            speak("Sorry, song not found")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?q=in&sortBy=publishedAt&pageSize=5&language=en&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            

            articles = data.get("articles", [])

            #Print the headlines
            if articles:
                speak("Here are the top headlines")
                print("Speaking top headlines")
                for article in articles[:5]:
                    title = article.get("title", "No title")
                    print("Headline:", title)
                    speak(title)
                    
            else:
                speak("No news articles found")
        else:
            speak("Failed to fetch news")
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)
        

           

    
#Main function 
if __name__ == "__main__":
    speak("Initializing Jarvis..")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
       
            

        print("recognizing..")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.3)
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Sir")
                #Listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.3)
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=5)
                    command = r.recognize_google(audio)

                    processCommand(command)



                    
        except Exception as e:
            print("Error; {0}".format(e))

       
