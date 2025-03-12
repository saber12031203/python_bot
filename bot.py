import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

BASE_URL = f"https://api.bale.ai/v1/bots/{436505518:e7DRmXeYKxmdBykhfhFEpDLHY8ojkzdEvZ4w3t63
}/"

def send_message(chat_id, text):
    url = BASE_URL + "sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        print("✅ پیام ارسال شد!")
    else:
        print(f"❌ خطا در ارسال پیام: {response.text}")

if __name__ == "__main__":
    chat_id = @miladfa  
    message_text = "سلام میلاد جان! من ربات ساختم، درسته؟ 😊"
    send_message(chat_id, message_text)
