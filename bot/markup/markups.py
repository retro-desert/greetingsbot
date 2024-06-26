from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from peewee import Model

from bot.services import get_all_titles, get_all_person


# Разметка отмены действия
def markup_cancel() -> ReplyKeyboardMarkup:
	# Добавление кнопки Назад в клавиатуре
	markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
	markup.add("Назад")
	return markup


def markup_to_menu() -> ReplyKeyboardMarkup:
	# Добавление кнопки Назад в клавиатуре
	markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
	markup.add("В меню")
	return markup


# Разметка основного меню
def markup_menu() -> InlineKeyboardMarkup:
	markup = InlineKeyboardMarkup(row_width=1)
	# Добавить две кнопки на сообщении
	item1 = InlineKeyboardButton("Выбрать праздник", callback_data="choose_event")
	item2 = InlineKeyboardButton("Внести свою дату", callback_data="input_event")
	markup.add(item1, item2)
	return markup


# Разметка выбора наименования праздника
def markup_choose_event() -> InlineKeyboardMarkup:
	markup = InlineKeyboardMarkup(row_width=1)
	# Выбор всех наименований и отображение их в виде кнопок на сообщении
	titles = get_all_titles()
	for i, title in enumerate(titles):
		markup.add(InlineKeyboardButton(text=title["name"], callback_data=f"event_{title['id']}"))
	return markup


# Разметка выбора человека для поздравления
def markup_choose_person(title: Model) -> InlineKeyboardMarkup:
	markup = InlineKeyboardMarkup(row_width=1)
	# Выбор всех личностей и отображение их в виде кнопок на сообщении
	persons = get_all_person(title=title)
	for i, person in enumerate(persons):
		markup.add(InlineKeyboardButton(text=person["name"], callback_data=f"for_{person['id']}"))
	return markup


# Разметка выбора поздравления
def markup_choose_greeting() -> ReplyKeyboardMarkup:
	# Добавление одной кнопки на сообщении
	markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
	markup.add("Еще поздравление", "Назад")
	return markup


# Разметка кнопки поддержать
def markup_donate(link: str = "https://www.google.com/", text: str = "Поддержать") -> InlineKeyboardMarkup:
	# Добавление кнопки с ссылкой "Поддержать" на сообщении
	markup = InlineKeyboardMarkup(row_width=1)
	item1 = InlineKeyboardButton(text=text, url=link)
	item2 = InlineKeyboardButton(text="В меню", callback_data="to_menu")
	markup.add(item1, item2)
	return markup
