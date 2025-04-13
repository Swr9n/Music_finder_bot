
import telebot
import subprocess

# توکن رباتت
bot = telebot.TeleBot('7781824174:AAHzrDH4KAJm78ZI-Wh4DaUrvz69WCqEme4')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! یه تیکه از متن آهنگ یا اسمشو بفرست تا برات پیداش کنم.")

@bot.message_handler(func=lambda message: True)
def search_music(message):
    query = message.text
    bot.reply_to(message, f"دارم دنبال آهنگ \"{query}\" می‌گردم...")

    try:
        result = subprocess.check_output(
            ['yt-dlp', f"ytsearch1:{query}", '--get-id', '--no-warnings'],
            stderr=subprocess.DEVNULL
        ).decode('utf-8').strip()

        if result:
            link = f"https://youtu.be/{result}"
            bot.send_message(message.chat.id, f"اینم نزدیک‌ترین نتیجه:\n{link}")
        else:
            bot.send_message(message.chat.id, "هیچی پیدا نکردم!")
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا هنگام جستجو:\n{e}")

bot.polling()
