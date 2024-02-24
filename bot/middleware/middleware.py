import datetime
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message
from bot.services.user import get_or_create_user


# Установить время последнего действия пользователя
async def set_user_activity(message: Message) -> bool:
	# Получить или создать пользователя
	obj = get_or_create_user(message.from_user.id, message.from_user.full_name)
	# Обновить дату последней активности
	obj.last_activity = datetime.datetime.utcnow()
	# Сохранить
	obj.save()
	return True


# Middleware действует при каждом полученном сообщении
class StatsMiddleware(BaseMiddleware):
	async def on_pre_process_message(self, message: Message, data: dict) -> bool:
		# Вызываем функцию при каждом входящем сообщении
		await set_user_activity(message)
		return True
