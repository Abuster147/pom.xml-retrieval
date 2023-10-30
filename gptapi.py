import openai

api_key = "sk-jQ4TJPBVL3cKd"

openai.api_key = api_key

conversation = []

print("Hey, Type 'exit' to end.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break

    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    bot_reply = response['choices'][0]['message']['content']
    print("ChatGPT: " + bot_reply)

    conversation.append({"role": "assistant", "content": bot_reply})
