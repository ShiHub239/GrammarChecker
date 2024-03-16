import time
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


    start = time.time()

    chat_completion = client.chat.completions.create (
        model ="gpt-3.5-turbo",
        messages = system_prompt + user_prompt, 
        temperature = 0,
        stream = True
    )

    piece_list = []
    message_list = []

    
    # response = chat_completion.choices[0].message.content
    response = chat_completion

    for piece in response:
        piece_time = time.time() - start
        piece_list.append(piece)
        list_message = piece.choices[0].delta.content
        message_list.append(list_message)
        print(f"Piece after {piece_time:.2f} seconds: {list_message}")



    # print(f"Your text: \n{response}")
