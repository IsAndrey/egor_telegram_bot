"""Бот Егора Макарова 2025 г."""

import os
import requests
import random
import datetime
from pprint import pprint
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater
from dotenv import load_dotenv

load_dotenv()

def random_date():
    """Получает случайную дату YYYY-MM-DD"""
    today = datetime.date.today()
    delta = (
        today-datetime.date(2000,1,1)
    ).days
    random_delta = random.randint(1, delta)
    return str(today - datetime.timedelta(days=random_delta))

def test_bot():
    """Посылает случайное фото в телеграм с сервера NASA"""
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    nasa_token = os.getenv('NASA_TOKEN')
    bot = Bot(token=telegram_token)
    bot.send_message(chat_id=telegram_chat_id, text='ПРИВЕТ')
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': nasa_token,
        'date': random_date()
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        json_data = response.json()
        pprint(json_data)

        if json_data['media_type'] == 'image':
            bot.send_photo(chat_id=telegram_chat_id, photo=json_data['url'])
        elif json_data['media_type'] == 'video':
            bot.send_video(chat_id=telegram_chat_id, video=json_data['url'])
        bot.send_message(chat_id=telegram_chat_id, text=json_data['title'])
    else:
        print(response.status_code)

def say_hi(update, context):
    """Обзовись"""
    telegram_chat_id = update['effective_chat']['id']
    context.bot.send_message(chat_id=telegram_chat_id,text='Привет, я Bobik!')
    context.bot.send_message(chat_id=telegram_chat_id, text='Охотник на котов и космический рэйнджер!')

def wake_up(update, context):
    """Бот подъем"""
    telegram_chat_id = update['effective_chat']['id']
    first_name = update['message']['chat']['first_name']
    buttons = ReplyKeyboardMarkup([['/hi'],['/cat'],['/space']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=telegram_chat_id,
        text=f'Здрастуйте уважаемый {first_name}-сан!',
        reply_markup=buttons
        )

def catch_cat(update, context):
    """Поймаем котика"""
    telegram_chat_id = update['effective_chat']['id']
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url=url)
    if response.status_code == 200:
        json_data = response.json()
        context.bot.send_photo(chat_id=telegram_chat_id, photo=json_data[0]['url'])

def investigate_space(update, context):
    """Исследуем космос"""
    telegram_chat_id = update['effective_chat']['id']
    nasa_token = os.getenv('NASA_TOKEN')
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': nasa_token,
        'date': random_date()
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        json_data = response.json()
        if json_data['media_type'] == 'image':
            context.bot.send_photo(chat_id=telegram_chat_id, photo=json_data['url'])
        elif json_data['media_type'] == 'video':
            context.bot.send_video(chat_id=telegram_chat_id, video=json_data['url'])
        context.bot.send_message(chat_id=telegram_chat_id, text=json_data['title'])

def run_bot():
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    bot = Updater(token=telegram_token)
    bot.dispatcher.add_handler(CommandHandler('start', wake_up))
    bot.dispatcher.add_handler(CommandHandler('hi', say_hi))
    bot.dispatcher.add_handler(CommandHandler('cat', catch_cat))
    bot.dispatcher.add_handler(CommandHandler('space', investigate_space))
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    run_bot()