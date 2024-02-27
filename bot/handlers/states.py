from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from dateutil import parser

from bot.handlers.commands import start
from bot.markup import markup_choose_greeting, markup_donate
from bot.markup import markup_cancel
from bot.services import create_event, get_default_event, get_photo, get_event_or_none
from bot.states import Form
from loader import bot


# Обработка сообщения при состоянии input_event_name
async def add_event_date(message: Message, state: FSMContext) -> None:
	# Формирование словаря с данными
	event_data = {"name": message.text}

	# Добавление словаря в сессионое хранилище
	await state.update_data(input_event_name=event_data)
	# Обновление состояния
	await Form.input_event_date.set()
	await bot.send_message(message.from_user.id, "(Добавление) Отправьте дату праздника в формате гггг мм дд",
						   reply_markup=markup_cancel())


# Обработка сообщения при состоянии input_event_date
async def add_event_final(message: Message, state: FSMContext) -> None:
	# Получение словаря из сессионного хранилища
	async with state.proxy() as data:
		event_data = data["input_event_name"]

	try:
		# Парсим дату из сообщения
		result_date = parser.parse(message.text)
	except Exception:
		await message.reply("Неверный формат даты")
		return None
	# Запись в БД
	create_event(
		id=message.from_user.id,
		name=message.from_user.full_name,
		title=event_data["name"],
		date=result_date
	)

	# Завершение состояния
	await state.finish()
	await bot.send_message(message.from_user.id, "[+] Праздник добавлен!\nПросмотреть - /show_events",
						   reply_markup=ReplyKeyboardRemove())


# Обработка сообщения при состоянии choose_greeting
async def choose_greeting(message: Message, state: FSMContext) -> None:
	# Если сообщение "Еще поздравление"
	if message.text == "Еще поздравление":
		# Достаем данные из состояния
		async with state.proxy() as data:
			event_data = data["choose_event"]
		# Выбираем праздник на основании полученных данных

		event = get_default_event(title=event_data['result'].split("_")[1], person=event_data['result'].split("_")[3])
		# Если итерация + 1 меньше кол-ва праздников
		if event_data["iter"] + 1 < event.count():
			# Выбираем праздник
			result = event.limit(event_data["iter"] + 2).dicts()[event_data["iter"] + 1]
			# Увеличиваем итерацию
			event_data["iter"] = event_data["iter"] + 1
			# Обновляем данные в состоянии
			await state.update_data(choose_event=event_data)
			# Отправляем фото с описанием
			await bot.send_photo(message.chat.id, get_photo(result["photo"]).photo_id,
								 caption=result["text"],
								 reply_markup=markup_choose_greeting())
		# Иначе
		else:
			# Завершение состояния
			await state.finish()
			# Сообщение
			text1 = """
А ещё, вы всегда сможете отправить поздравление с праздником для семей фонда Соломон! А в знак благодарности мы с удовольствием отправим вам письмо радости от подопечного или видео привет!
Нажмите на кнопку - чтобы поддержать семью"""
			# await bot.send_message(message.chat.id, text2, reply_markup=ReplyKeyboardRemove())
			await bot.send_message(message.chat.id, text1, reply_markup=markup_donate(link="https://clck.ru/394XDH/"))
			await start(message, state)


# Обработка сообщения при состоянии del_event
async def del_event_final(message: Message, state: FSMContext) -> None:
	# Достаем информацию из состояния
	async with state.proxy() as data:
		event_data = data["del_event"]
	# Если полученное сообщение есть в информации из состояния
	if message.text in event_data:
		# Если праздник действительно есть в БД, иначе ничего
		result = get_event_or_none(user_id=message.from_user.id, event_id=event_data[message.text])

		# Если результат есть
		if result:
			# Удаляем полученное значение
			result.delete_instance()
			# Отвечаем пользователю
			await message.reply("[+] Праздник удален", reply_markup=ReplyKeyboardRemove())
			# Завершение состояния
			await state.finish()
	# Иначе
	else:
		await bot.send_message(message.from_user.id, "[-] Праздник не найден, попробуйте еще раз")


def register_states(disp: Dispatcher) -> list:
	# Регистрируем обработчики
	disp.register_message_handler(add_event_date, state=Form.input_event_name)
	disp.register_message_handler(add_event_final, state=Form.input_event_date)
	disp.register_message_handler(choose_greeting, state=Form.choose_greeting)
	disp.register_message_handler(del_event_final, state=Form.del_event)

	return []
