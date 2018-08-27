import telebot
import os
token = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(token)

# A helper to get rid of the /command
def get_text(full_text):
    text_parts = full_text.split()
    return ' '.join(text_parts[1:])

# Method to connect to the sentiment model
def get_sentiment(text):
    response = requests.post('http://text-processing.com/api/sentiment/',
             data={'text':text})
    response_data = response.json()
    return response_data['label']

# Sentiment command handler
@bot.message_handler(commands=['sent'])
def sentiment(message):
    text = get_text(message.text)
    text_sentiment = get_sentiment(text)
    if text_sentiment == 'pos':
        reply = 'Your text is positive'
    elif text_sentiment == 'neg':
        reply = 'Your text is negative'
    else:
        reply = 'Your text is neutral'
    bot.send_message(message.chat.id, text=reply)

# Any command handler
@bot.message_handler()
def say_hello(message):
    print(message)
    bot.send_message(message.chat.id, text='It works')

bot.polling()
