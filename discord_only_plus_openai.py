from dotenv import load_dotenv
from openai import OpenAI # OpenAI library
import discord
import os

#set openai api key
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')
oa_client = OpenAI(api_key=OPENAI_KEY)

# ask openai - respond like a pirate
def call_openai(question):
  # Call the OpenAI API
  completion = oa_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": f"Respond like a pirate to the following question: {question}, 
        },
    ]
  )

# Print the response
  response = comlpetion.choices[0].message.content
  print(response)
  return response
  
# Load environment variables from .env file
load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure that your bot can read message content
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

client.run(os.getenv('TOKEN'))
