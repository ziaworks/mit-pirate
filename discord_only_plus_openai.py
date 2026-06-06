from dotenv import load_dotenv
from openai import OpenAI
import discord
import os

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')
DISCORD_TOKEN = os.getenv('TOKEN')

oa_client = OpenAI(api_key=OPENAI_KEY)

def call_openai(question):
    completion = oa_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": f"Respond like a pirate to the following question: {question}",
            },
        ]
    )
    response = completion.choices[0].message.content
    print(response)
    return response

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$question'):
        print(f"Message: {message.content}")
        message_content = message.content.split("$question", 1)[1].strip()
        print(f"Question: {message_content}")
        response = call_openai(message_content)
        print(f"Assistant: {response}")
        print("---")
        await message.channel.send(response)

client.run(DISCORD_TOKEN)
