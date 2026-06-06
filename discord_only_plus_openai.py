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

if message.content.startswith('$question'):
        print(f"Message: {message.content}")
        message_content = message.content.split("$question")[1]
        print(f"Question: {message_content}")
        response = call_openai(message_content)
        print(fAssistant: {response}")
        print("---")
        await message.channel.send(response)

client.run(os.getenv('TOKEN'))


