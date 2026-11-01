from google import genai
import telebot

TELEGRAM_TOKEN = "8633513758:AAGbpYbtrJKNCbj-nb72sXvwmGJF1PoygHk"
GEMINI_KEY = "dummy"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
gemini_client = genai.Client(api_key=GEMINI_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your personal Gemini AI assistant on Telegram.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        response = gemini_client.models.generate_content(
            model="gemini-flash-latest",
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

print("Telegram Gemini Bot is online and listening...")
bot.infinity_polling()
