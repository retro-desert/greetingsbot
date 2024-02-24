import datetime

from peewee import Model

from bot.services import get_user, get_or_create_user
from models import Event


# Получение всех праздников пользователя
def get_all_events(user_id: int) -> list:
	events = [event for event in Event.select(Event.id, Event.text, Event.date).where(Event.is_default == False,
																					  Event.user == get_user(
																						  user_id)).dicts()]
	if not events:
		return []

	return events


# Получить праздник или нет
def get_event_or_none(user_id: int, event_id: int) -> Model:
	result = Event.get_or_none(Event.is_default == False, Event.user == get_user(user_id),
							   Event.id == event_id)
	return result


# Получаем поздравление
def get_event(id: int) -> Model:
	event = Event.get(Event.title == id)
	return event


# Получение конкретного дефолтного поздравления по данным
def get_default_event(title: int, person: int) -> Model:
	event = Event.select(Event.text, Event.photo).where(Event.is_default == True,
														Event.title == title,
														Event.person == person)
	return event


# Создать праздник
def create_event(id: int, name: str, title: str, date: datetime.datetime):
	Event.create(
		user=get_or_create_user(id, name=name),
		text=title,
		date=date
	).save()
