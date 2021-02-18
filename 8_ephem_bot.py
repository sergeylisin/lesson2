"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def planet(update,context):
  planets = ["Mercury","Venus", "Mars", "Moon", "Jupyter","Saturn","Neptune","Uranus"]
  txt = update.message.text
  planet = txt.split()[1]
  if planet not in planets:
    update.message.reply_text("unknown planet")
  else:
    print(planet)
    if planet == "Mercury":
      p = ephem.Mercury()
    elif planet == "Venus":
      p = ephem.Venus()
    elif planet == "Mars":
      p = ephem.Mars()
    elif planet == "Moon":
      p = ephem.Moon()
    elif planet == "Jupyter":
      p = ephem.Jupyter()
    elif p == "Saturn":
      p = ephem.Saturn()
    elif planet == "Neptune":
      p = ephem.Neptune()
    elif planet == "Uranus":
      p = ephem.Uranus()
    p.compute()
    constellation = ephem.constellation(p)[1]
    print(constellation)
    update.message.reply_text(constellation)


def main():
    mybot = Updater('1521578217:AAEnXxtMOFj1Y_1IhHAjVQBR5sRtRxVpC2w', request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
