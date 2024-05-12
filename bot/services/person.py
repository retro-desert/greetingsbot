from peewee import Model
from models import Person


def get_all_person(title: Model) -> list:
	# Получение всех персон
	persons = [person for person in Person.select().where(Person.title == title).order_by(Person.place).distinct().dicts()]
	return persons
