
import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = "6192062611:AAFDEfu4lMdHUqoX8Iz6dEB-hcOnfip0hSc"  # استبدل "YOUR_TOKEN" بتوكن البوت الخاص بك
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    inline_keyboard = InlineKeyboardMarkup()
    inline_keyboard.add(InlineKeyboardButton("المطور", url="https://t.me/SSGA56"))
    bot.send_message(
        message.chat.id,
        "- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .",
        reply_markup=inline_keyboard,
    )

@bot.message_handler(func=lambda m: True)
def send(message):
    bot.send_message(message.chat.id, "<strong>Wait Please</strong>", parse_mode="html")
    url = requests.get(f"https://apiss.mhmd-mnyrmnyr.repl.co/down.php?url={message.text}").json()
    io = url["result"]["download"]
    li = url["result"]["like"]
    co = url["result"]["comment"]
    sh = url["result"]["share"]
    cr = url["result"]["created"]
    by = url["source"]
    bot.send_video(
        message.chat.id,
        io,
        caption=f"""
        Done ✅
        لايكات : {li}
        تعليقات : {co}
        مشاركة : {sh}
        نشر بتاريخ : {cr}
        البوت : { user_bot }
        """,
    )


bot.polling()
