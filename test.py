import telebot, random

TOKEN = '779301632:AAFgNRWhrHd3TN5nX7XYvwX1jmUi3HMTRVQ'

bot = telebot.TeleBot(TOKEN)

smiles = [
'😀',
'❤️',
'😍',
'🤣'
]

@bot.message_handler(commands=['start','help'])
def answer(message):
  if message.from_user.id != 686540479:
   bot.reply_to(message, "hello")
  else:
   bot.reply_to(message, "Poka")

@bot.message_handler(func = lambda message: True)
def uppper(message):
  bot.reply_to(message, random.choice(smiles))



bot.polling()
