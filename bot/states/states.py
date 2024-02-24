from aiogram.dispatcher.filters.state import StatesGroup, State


# Состояния
class Form(StatesGroup):
	del_event = State()
	choose_event = State()
	input_event = State()
	input_event_name = State()
	input_event_date = State()
	choose_person = State()
	choose_greeting = State()
	create_message = State()