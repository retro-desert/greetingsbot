from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import BotCommand, Message, ParseMode, ReplyKeyboardRemove
from bot.markup import markup_menu, markup_cancel
from bot.services import get_all_events
from bot.states import Form
from loader import bot


# Обработка команды /start, начало
async def start(message: Message, state: FSMContext) -> None:
	# Завершаем все состояния
	await state.finish()
	# Текст сообщения
	text = """
Привет! Этот бот создал фонд Соломон! Здесь мы заботимся о том, чтобы ни одна важная дата в вашей жизни не забылась.
У нас готовы поздравления, которые можно отправить вашим друзьям, коллегам или тем, кого вы любите. Выбирайте и делитесь!
А если у вас есть своя особенная дата, которая заслуживает внимания, добавьте ее сюда, и за два дня мы напомним вам о ней.
"""
	# Отвечаем пользователю
	await message.reply(text,
						parse_mode=ParseMode.HTML,
						reply_markup=markup_menu())


# Обработка команды /help
async def help(message: Message, state: FSMContext) -> None:
	# Завершаем все состояния
	await state.finish()
	# Текст сообщения
	text = """Список команд
/start - Приветственное сообщение, перезапуск
/help - Это сообщение
/cancel - Отмена действия, выход
/show_events - Показать все праздники
/add_event - Добавить праздник
/del_event - Удалить праздник"""
	# Пишем пользователю
	await bot.send_message(message.from_user.id, text,
						   reply_markup=ReplyKeyboardRemove())


# Обработка команды /cancel
async def cancel(message: Message, state: FSMContext) -> None:
	# Завершаем все состояния
	await state.finish()
	# Отвечаем пользователю
	await message.reply("[+] Сброшено", reply_markup=ReplyKeyboardRemove())


# Обработка команды /show_events
async def show_events(message: Message) -> None:
	# Получаем все праздники пользователя
	events = get_all_events(message.from_user.id)

	# Если праздники есть
	if events:
		events = [f"Праздник: {event['text']}\nДата: {event['date']}" for event in events]
		await message.reply("\n\n".join(events))
	# Иначе
	else:
		await message.reply("[-] Добавленных праздников нет")


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
		await message.reply(f"[*] 1/1 (Удаление) Выберите праздник из списка:\n{result_list}",
							reply_markup=markup_cancel())
	# Иначе
	else:
		await message.reply("[-] Добавленных праздников нет")


# Обработка полученного фото
# @disp.message_handler(state="*", content_types=["photo"])
# async def rwedwedphoto(message: types.Message) -> None:
# 	print(message.photo)


# Обработка команды /add_event
async def add_event_name(message: Message) -> None:
	# Установка состояния
	await Form.input_event_name.set()
	await bot.send_message(message.from_user.id, "[*] 1/2 (Добавление) Отправьте название праздника",
						   reply_markup=markup_cancel())


def register_commands(disp: Dispatcher) -> list:
	# Наименования команд
	start_command_name = "start"
	help_command_name = "help"
	cancel_command_name = "cancel"
	show_events_command_name = "show_events"
	add_event_name_command_name = "add_event"
	del_event_command_name = "del_event"

	# Регистрируем обработчики
	disp.register_message_handler(start, commands=[start_command_name], state="*")
	disp.register_message_handler(help, commands=[help_command_name], state="*")
	disp.register_message_handler(cancel, commands=[cancel_command_name], state="*")
	disp.register_message_handler(show_events, commands=[show_events_command_name])
	disp.register_message_handler(add_event_name, commands=[add_event_name_command_name])
	disp.register_message_handler(del_event_begin, commands=[del_event_command_name])

	# Возвращаем список команд
	return [
		BotCommand(start_command_name, "Приветственное сообщение, перезапуск"),
		BotCommand(help_command_name, "Список команд"),
		BotCommand(cancel_command_name, "Отмена действия, выход"),
		BotCommand(show_events_command_name, "Показать все праздники"),
		BotCommand(add_event_name_command_name, "Добавить праздник"),
		BotCommand(del_event_command_name, "Удалить праздник"),
	]
