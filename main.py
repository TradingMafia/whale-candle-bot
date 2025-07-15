import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
channel_username = os.getenv("CHANNEL_USERNAME")

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=[]))  # We'll add source channels later
async def handler(event):
    message = event.raw_text

    # Example filter: ignore if message contains social links
    blocked_keywords = ["youtube.com", "instagram.com", "t.me", "twitter.com"]
    if any(x in message.lower() for x in blocked_keywords):
        return

    # Example format
    message = message.replace("#", "")  # remove hashtags
    message += "\n\n🔔 Posted by Whale Candle FX"

    await client.send_message(channel_username, message)

print("Bot is running...")
client.run_until_disconnected()
