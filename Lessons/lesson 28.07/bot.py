import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot = telebot.TeleBot("5534693498:AAHpDo9quwS6rrxCOQkYcp5ZA0VwNjrOO3g")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello there!")

@bot.message_handler(commands=['update'])
def start_message(message):

    html = urlopen("https://kurs.onliner.by/")
    soup = BeautifulSoup(html)

    tag_list = soup.findAll('span', {'class':'value rise'})

    buy = tag_list[0].text
    sell = tag_list[1].text
    nb = tag_list[2].text

    bot.send_message(message.chat.id, buy + ", " + sell + ", " + nb)

bot.polling()