import os
from openai import OpenAI
import re
from dotenv import load_dotenv


load_dotenv()


client = OpenAI()

system_prompt = [{
    "role": "system", 
    "content" : "You are a grammar checker that looks for mistakes and makes sentence’s more fluent. You take all the users input and auto correct it. Just reply to user input with the correct grammar, DO NOT reply the context of the question of the user input. If the user input is grammatically correct and fluent, just reply “sounds good”. Sample of the conversation will show below:"
}]

while(True):
    user_input = input("Please enter your text: \n")

    if user_input == "exit":
        break

    user_prompt = [{
        "role": "user",
        "content": user_input
    }]

    chat_completion = client.chat.completions.create (
        model ="gpt-3.5-turbo",
        messages = system_prompt + user_prompt, 
        temperature = 0
    )

    response = chat_completion.choices[0].message.content
    print(f"Your text: \n{response}")
