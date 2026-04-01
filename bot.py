import requests
import time
from telegram import Bot
from datetime import datetime

TOKEN = "8752995907:AAElrSgEM2-QkCOrM1baWT34Sgee7pCgVI8"
CHAT_ID = "-1003896922442

bot = Bot(token=TOKEN)

last_men = 0
last_women = 0

def get_data():
    # ⚠️ Yaha real scraping / API lagana hoga
    # Demo data (random change)
    import random
    men = random.randint(300, 400)
    women = random.randint(1500, 1700)
    return men, women

def format_message(men, women, diff_men, diff_women):
    time_now = datetime.now().strftime("%d %b %Y, %I:%M %p")

    msg = f"""🔔 Shein Stock Update

👨 Men → {men} {'🔺+'+str(diff_men) if diff_men>0 else ''}
👩 Women → {women} {'🔺+'+str(diff_women) if diff_women>0 else ''}

⏰ {time_now}

🔗 Direct Link: https://www.sheinindia.in/
"""
    return msg

while True:
    try:
        men, women = get_data()

        diff_men = men - last_men
        diff_women = women - last_women

        if last_men != 0:  # first time skip
            message = format_message(men, women, diff_men, diff_women)
            bot.send_message(chat_id=CHAT_ID, text=message)

        last_men = men
        last_women = women

        time.sleep(300)  # 5 min
    except Exception as e:
        print("Error:", e)
        time.sleep(60)
