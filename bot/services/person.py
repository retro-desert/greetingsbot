from models import Person


def get_all_person() -> list:
	# Получение всех персон
	persons = [person for person in Person.select().order_by(Person.place).distinct().dicts()]
	return persons
