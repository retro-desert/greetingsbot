from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.handlers.commands import start
from bot.markup import markup_choose_event, markup_cancel, markup_donate, markup_choose_person, markup_choose_greeting
from bot.services import get_event, get_title, get_photo, get_default_event
from bot.states import Form
from loader import bot


# Обработка колбеков
async def choose_event_callback(call: CallbackQuery, state: FSMContext) -> None:
	# Если есть колбек
	if call.message:
		# Завершаем состояние
		await state.finish()
		# Если choose_event есть в данных колбека
		if "choose_event" in call.data:
			# Установка состояния
			await Form.choose_event.set()
			# Отправка сообщения
			await bot.send_message(call.message.chat.id, "Выбери праздник", reply_markup=markup_choose_event())
		# Если input_event есть в данных колбека
		elif "input_event" in call.data:
			# Установка состояния
			await Form.input_event_name.set()
			# Отправка сообщения
			await bot.send_message(call.message.chat.id, "(Добавление) Отправьте название праздника",
								   reply_markup=markup_cancel())


# Обработка колбеков при состоянии choose_event
async def choose_person_callback(call: CallbackQuery, state: FSMContext) -> None:
	# Если есть колбек
	if call.message:
		# Если event_ есть в данных колбека
		if "event_" in call.data:
			# Установка состояния
			await Form.choose_person.set()
			# Находим праздник
			event = get_event(int(call.data.split("_")[1]))
			# Находим наименование
			title = get_title(int(call.data.split("_")[1]))
			# Увеличиваем кол-во нажатий
			title.tap_count += 1
			title.save()

			# Если у праздника есть кнопка
			if event.button_link:
				# Отправляем фото с описанием
				await bot.send_photo(call.message.chat.id, get_photo(event.photo).photo_id,
									 caption=event.text,
									 reply_markup=markup_donate(text=event.button_text, link=event.button_link))
				await start(call.message.chat.id, state)
			# Иначе
			else:
				# Формируем словарь с данными
				event_data = {"name": call.data}
				# Обновляем данные в состоянии
				await state.update_data(choose_event=event_data)
				await bot.send_message(call.message.chat.id, "Кого мы поздравляем?",
									   reply_markup=markup_choose_person())


# Обработка колбеков при состоянии choose_person
async def choose_greeting_callback(call: CallbackQuery, state: FSMContext) -> None:
	# Если есть колбек
	if call.message:
		# Если "for_" есть в данных колбека
		if "for_" in call.data:
			# Получаем информацию из состояния
			async with state.proxy() as data:
				event_data = data["choose_event"]

			# Формируем словарь данных
			result = f"{event_data['name']}_{call.data}"
			# Выбираем поздравление
			event = get_default_event(title=int(event_data['name'].split("_")[1]), person=int(call.data.split("_")[1])).dicts()[0]
			# Обновляем данные в состоянии
			await state.update_data(choose_event={"result": result, "iter": 0})

			await bot.send_message(call.message.chat.id, "Выбери поздравление для этого человека")
			await bot.send_photo(call.message.chat.id, get_photo(event["photo"]).photo_id,
								 caption=event["text"],
								 reply_markup=markup_choose_greeting())
			# Установка состояния
			await Form.choose_greeting.set()


def register_callbacks(disp: Dispatcher) -> list:
	# Регистрируем обработчики
	disp.register_callback_query_handler(choose_event_callback)
	disp.register_callback_query_handler(choose_person_callback, state=Form.choose_event)
	disp.register_callback_query_handler(choose_greeting_callback, state=Form.choose_person)
	disp.register_callback_query_handler(choose_greeting_callback, state=Form.choose_person)

	return []
