from aiogram import Bot, Dispatcher, types
from peewee import PostgresqlDatabase
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from data import config

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

psql_db = PostgresqlDatabase(
            config.DATABASE,
            user=config.USER,
            password=config.PASSWORD,
            host=config.HOST,
            port=config.PORT
        )

storage = RedisStorage2(config.REDIS_HOST, config.REDIS_PORT, db=5)

disp = Dispatcher(bot, storage=storage)
