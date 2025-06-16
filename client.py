from openai import OpenAI
# pip install openai

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

completion = client.chat.completions.create(
    model="llama3-8b-8192",  # or llama3-70b-8192
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa, Siri and GoogleCloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)

