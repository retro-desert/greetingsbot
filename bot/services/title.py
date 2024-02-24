from models import Title
from peewee import Model


# Получаем самое популярное поздравление
def get_popular_greeting() -> list:
	# Выбираем самое популярное наименование поздравления
	greeting = [i for i in Title.select(Title.name).order_by(Title.tap_count.desc()).limit(1).dicts()]
	return greeting


# Поулчаем все наименования
def get_all_titles() -> list:
	# Выбираем все наименования
	titles = [title for title in
			  Title.select().where(Title.is_default == True).order_by(Title.place).distinct().dicts()]
	return titles


# Получаем наименование
def get_title(id: int) -> Model:
	title = Title.get(Title.id == id)
	return title
