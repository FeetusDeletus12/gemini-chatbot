import requests
import json


def chat_with_gemini(user_input, history):
    API_KEY = "AIzaSyDIC3cUDgmBoFnx0vZDHH3g0IyawU4zQD0"  # Replace with your actual API key
    URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"

    headers = {"Content-Type": "application/json"}

    # System message to instruct the AI on how to behave
    system_message = "You are a helpful, knowledgeable chatbot named Gemini. You can assist with anything, including coding, tech support, general advice, and casual conversation. Keep responses clear, concise, and adapt your tone based on the user's approach. If the user greets you casually, respond casually. If they ask professionally, respond formally. Keep responses medium-length unless asked otherwise."

    # Keep only the last 10 exchanges to limit memory usage
    history = history[-10:]

    parts = [{"text": system_message}] + [{"text": msg} for msg in history]  # Include system message and history
    parts.append({"text": user_input})  # Add new user input

    data = {"contents": [{"parts": parts}]}
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    result = response.json()
    response_text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text",
                                                                                                   "Error getting response")

    return response_text


def main():
    print("Chat with Gemini AI (Gemini 1.5 Pro). Type 'exit' to quit.")
    history = []  # Store conversation history

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = chat_with_gemini(user_input, history)
        history.append(f"You: {user_input}")
        history.append(f"Gemini: {response}")

        print(f"Gemini: {response}")


if __name__ == "__main__":
    main()
