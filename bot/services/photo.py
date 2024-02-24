from models import Photo
from peewee import Model


# Получаем фото
def get_photo(id: int) -> Model:
	photo = Photo.get(Photo.id == id)
	return photo
