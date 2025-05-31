from django.conf import settings
from datetime import datetime, timedelta
import requests
from apps.bot.config import bot

CHANNEL_ID = settings.CHANNEL_ID
BOT_TOKEN = settings.BOT_TOKEN


def generate_one_time_link():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/createChatInviteLink"

    data = {
        "chat_id": CHANNEL_ID,
        "member_limit": 1,
        "expire_date": int((datetime.now() + timedelta(days=30)).timestamp())
    }

    response = requests.post(url, json=data)
    invite_link = response.json().get('result').get('invite_link')
    return invite_link


async def send_broadcast(user_id, ad):
    try:
        make_url = f"https://reklama.icc-kimyo.uz/{ad.image.url}"
        caption = f"{ad.caption}"

        await bot.send_photo(user_id, photo=make_url, caption=caption, parse_mode="HTML")
    except Exception as e:
        print(f"Error sending broadcast to member {user_id}: {str(e)}")
