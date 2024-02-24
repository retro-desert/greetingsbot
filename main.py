# TODO: текста и ссылки вынести в бд
import asyncio
import logging
from typing import List

from aiogram.types import BotCommand

from bot.filters import AdminFilter
from bot.handlers.admin import register_admin
from bot.handlers.callbacks import register_callbacks
from bot.handlers.commands import register_commands
from bot.handlers.states import register_states
from bot.middleware import StatsMiddleware
from loader import disp


def register_all_filters():
	disp.filters_factory.bind(AdminFilter)


def register_all_middleware():
	disp.middleware.setup(StatsMiddleware())


def register_all_handlers() -> List[BotCommand]:
	all_commands: List = []
	handlers = [register_admin, register_commands, register_callbacks, register_states]
	for handler in handlers:
		commands = handler(disp)
		all_commands.extend(commands)
	return all_commands


async def set_my_commands(commands: List[BotCommand]):
	await disp.bot.set_my_commands(commands)


async def stop_bot():
	await disp.storage.close()
	await disp.storage.wait_closed()
	session = await disp.bot.get_session()
	await session.close()


async def init_bot():
	register_all_filters()
	register_all_middleware()
	commands = register_all_handlers()
	await set_my_commands(commands)


async def main():
	logging.basicConfig(level=logging.INFO)
	await init_bot()

	try:
		await disp.start_polling()
	finally:
		await stop_bot()


if __name__ == "__main__":
	try:
		asyncio.run(main())
	except Exception as e:
		logging.error(e)
