import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers.openai.chat_gpt3_5 import OpenAIHandler
from handlers.schedule.parse_schedule import ScheduleHandler

import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

openai_handler = OpenAIHandler()
parse_schedule_handler = ScheduleHandler()

bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

dp.register_message_handler(openai_handler.handle_message)
dp.register_message_handler(parse_schedule_handler.handle_message)

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)