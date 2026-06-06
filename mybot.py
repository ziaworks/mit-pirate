from dotenv import load_dotenv
from openai import OpenAI
import discord
import os

# Load environment variables from .env file
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')
DISCORD_TOKEN = os.getenv('TOKEN')

# Initialize the OpenAI client
openai_client = OpenAI(api_key=OPENAI_KEY)

def call_openai(question):
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
             {
                 "role": "user",
                 "content": f"Respond like a pirate to the following question:  {question}",
            },
        ]
    )
    # Print the response
    response = completion.choices[0].message.content
    print(response)
    return response


# Set up discord
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
        if not message_content:
            await message.channel.send('Arr, ask me a question after `$question`, matey!')
            return
        print(f"Question: {message_content}")
        try:
            response = call_openai(message_content)
            print(f"Assistant: {response}")
            print("---")
            await message.channel.send(response)
        except Exception as e:
            print(f"OpenAI error: {e}")
            await message.channel.send(
                'Blimey! Me OpenAI treasure chest be empty. '
                'Check yer API key and billing at https://platform.openai.com/account/billing'
            )

client.run(DISCORD_TOKEN)
