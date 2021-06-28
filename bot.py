from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from imgkit.api import from_file
from aiogram.types import input_file
from config import TOKEN
from bs4 import BeautifulSoup
import requests
import imgkit
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
URL = 'https://phdpu.edu.ua/course/oo-11pm-e-12pm-f-13pm-pv/'
page = requests.get(URL)
  # load the page content
text = page.content
  
soup = BeautifulSoup(text, "html.parser")
with open("output.html", "w", encoding = 'utf-8') as file:
css='style.css'
imgkit.from_file('output.html',options=options,css=css, 'catd.jpg')
    
@dp.message_handler(commands=['start', 'help'])

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я тебе расписания")

@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id,types.input_file.InputFile('catd.jpg'))

if __name__ == '__main__':
    executor.start_polling(dp)
