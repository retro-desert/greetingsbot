from aiogram import Dispatcher

from bot.markup import markup_cancel
from loader import bot
from aiogram.types import Message, BotCommand, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from bot.states import Form
from bot.services import get_users, count_users, get_active_users, get_popular_greeting


# Обработка команды /help, только админы
async def admin_help(message: Message, state: FSMContext) -> None:
	# Завершаем все состояния
	await state.finish()
	# Сообщение
	text = """Список админ команд
/all_users - Кол-во всех пользователей
/all_active_users - Количество активных пользователей
/popular_greeting - Самое популярное поздравление
/create_message - Создать сообщение
"""
	# Пишем пользователю
	await bot.send_message(message.from_user.id, text,
						   reply_markup=ReplyKeyboardRemove())


# Обработка команды /all_users, только админы
async def all_users(message: Message) -> None:
	# Отвечаем пользователю
	await message.reply(f"Кол-во всех пользователей: {count_users()}")


# Обработка команды /all_active_users, только админы
async def all_active_users(message: Message) -> None:
	# Выбирем кол-во пользователей, у которых дата последней активности меньше недели назад
	amount = get_active_users()
	# Отвечаем пользователю
	await message.reply(f"Кол-во активных за неделю пользователей: {amount}")


# Обработка команды /popular_greeting, только админы
async def popular_greeting(message: Message) -> None:
	# Выбираем самое популярное наименование поздравления
	greeting = get_popular_greeting()
	await message.reply(f"Самое популярное поздравление: {greeting[0]['name']}")


# Обработка команды /create_message, только админы
async def create_message(message: Message) -> None:
	# Установить состояние
	await Form.create_message.set()
	await message.reply(f"Напишите сообщение, которое вы хотите разослать всем пользователям",
						reply_markup=markup_cancel())


# Обработка сообщения при состоянии create_message, только админы
async def create_message_second(message: Message, state: FSMContext) -> None:
	# Каждому пользователю отправляем сообщение
	for user in get_users():
		await bot.send_message(str(user), message.text)
	# Сообщаем об успешной отправке, убираем разметку
	await message.reply("[+] Успешно отправлено", reply_markup=ReplyKeyboardRemove())
	# Завершаем состояние
	await state.finish()


def register_admin(disp: Dispatcher) -> list:
	# Наименования команд
	admin_help_command_name = "admin_help"
	all_users_command_name = "all_users"
	all_active_users_command_name = "all_active_users"
	popular_greeting_command_name = "popular_greeting"
	create_message_command_name = "create_message"

	# Регистрируем обработчики
	disp.register_message_handler(admin_help, commands=[admin_help_command_name], state="*", is_admin=True)
	disp.register_message_handler(all_users, commands=[all_users_command_name], is_admin=True)
	disp.register_message_handler(all_active_users, commands=[all_active_users_command_name], is_admin=True)
	disp.register_message_handler(popular_greeting, commands=[popular_greeting_command_name], is_admin=True)
	disp.register_message_handler(create_message, commands=[create_message_command_name], is_admin=True)
	disp.register_message_handler(create_message_second, state=Form.create_message, is_admin=True)

	# Возвращаем список команд
	return [
		# BotCommand(admin_help_command_name, "Админ команды"),
		# BotCommand(all_users_command_name, "Кол-во всех пользователей"),
		# BotCommand(all_active_users_command_name, "Кол-во активных пользователей"),
		# BotCommand(popular_greeting_command_name, "Самое популярное поздравление"),
		# BotCommand(create_message_command_name, "Создать сообщение для всех"),
	]
