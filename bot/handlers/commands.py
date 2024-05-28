from datetime import datetime

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import BotCommand, Message, ParseMode, ReplyKeyboardRemove
from bot.markup import markup_menu, markup_cancel
from bot.services import get_all_events
from bot.states import Form
from loader import bot


# Обработка команды /start, начало
async def start(message: Message or int, state: FSMContext) -> None:
	# Завершаем все состояния
	await state.finish()
	# Текст сообщения
	text1 = """
Привет. Этот бот создал фонд Соломон. Здесь мы заботимся о том, чтобы ни одна важная дата в вашей жизни не забылась.\n
У нас готовы поздравления, которые можно отправить вашим друзьям, коллегам или тем, кого вы любите. Выбирайте и делитесь.\n
А если у вас есть своя особенная дата, которая заслуживает внимания, добавьте ее сюда, и за два дня мы напомним вам о ней.
"""
	text2 = """Начнем❤️"""
	# Отвечаем пользователю

	await bot.send_message(message.from_user.id if type(message) == Message else message,
						   text1,
						parse_mode=ParseMode.HTML,
						reply_markup=ReplyKeyboardRemove())
	await bot.send_message(message.from_user.id if type(message) == Message else message,
						   text2,
						   reply_markup=markup_menu())


# Обработка команды /help
async def help(message: Message, state: FSMContext) -> None:
	# Завершаем все состояния
	await state.finish()
	# Текст сообщения
	text = """Список команд
/start - Приветственное сообщение, перезапуск
/help - Это сообщение
/show_events - Показать все праздники
/add_event - Добавить праздник
/del_event - Удалить праздник"""
	# Пишем пользователю
	await bot.send_message(message.from_user.id, text,
						   reply_markup=ReplyKeyboardRemove())


# Обработка команды /show_events
async def show_events(message: Message) -> None:
	# Получаем все праздники пользователя
	events = get_all_events(message.from_user.id)

	# Если праздники есть
	if events:
		events = [f"Праздник: {event['text']}\nДата: {datetime.strftime(event['date'], '%d.%m.%Y')}" for event in events]
		await message.reply("\n\n".join(events))
	# Иначе
	else:
		await message.reply("Добавленных праздников нет")


# Обработка команды /del_event
async def del_event_begin(message: Message, state: FSMContext) -> None:
	# Установка состояния
	await Form.del_event.set()
	# Получаем все праздники пользователя
	events = get_all_events(message.from_user.id)

	# Если праздники есть
	if events:
		# Выводим отформатированный список праздников
		result_list = "\n\n".join([f"{i}) {events[i]['text']}\n{events[i]['date']}" for i in range(len(events))])
		# Обновление информации в состоянии
		await state.update_data(del_event={str(i): events[i]["id"] for i in range(len(events))})
		# Отвечаем пользователю
		await message.reply(f"Выберите праздник из списка:\n{result_list}",
							reply_markup=markup_cancel())
	# Иначе
	else:
		await message.reply("Добавленных праздников нет")


# Обработка команды /add_event
async def add_event_name(message: Message) -> None:
	# Установка состояния
	await Form.input_event_name.set()
	await bot.send_message(message.from_user.id, "Отправьте название праздника",
						   reply_markup=markup_cancel())


def register_commands(disp: Dispatcher) -> list:
	# Наименования команд
	start_command_name = "start"
	help_command_name = "help"
	show_events_command_name = "show_events"
	add_event_name_command_name = "add_event"
	del_event_command_name = "del_event"

	# Регистрируем обработчики
	disp.register_message_handler(start, commands=[start_command_name], state="*")
	disp.register_message_handler(help, commands=[help_command_name], state="*")
	disp.register_message_handler(show_events, commands=[show_events_command_name])
	disp.register_message_handler(add_event_name, commands=[add_event_name_command_name])
	disp.register_message_handler(del_event_begin, commands=[del_event_command_name])

	# Возвращаем список команд
	return [
		BotCommand(start_command_name, "Приветственное сообщение, перезапуск"),
		BotCommand(help_command_name, "Список команд"),
		BotCommand(show_events_command_name, "Показать все свои праздники"),
		BotCommand(add_event_name_command_name, "Добавить праздник"),
		BotCommand(del_event_command_name, "Удалить праздник"),
	]
