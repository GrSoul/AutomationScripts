#!/usr/bin/python3
# Make it executable: chmod +x <filename.py>
# Run with ./<filename.py> or double click

import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")