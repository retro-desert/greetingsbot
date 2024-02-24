from peewee import fn
from data.config import ADMINS
from models import TgUser
from datetime import datetime, timedelta


# Кол-во пользователей
def count_users() -> int:
    query = TgUser.select(fn.COUNT(TgUser.id))
    return query.scalar()


# Получить всех пользователей
def get_users() -> list[TgUser]:
    query = TgUser.select()
    return list(query)


# Получить пользователя
def get_user(id: int) -> TgUser:
    return TgUser.get_or_none(TgUser.id == id)


# Создать пользователя
def create_user(id: int, name: str) -> TgUser:
    new_user = TgUser.create(id=id, name=name, created_at=datetime.utcnow())
    if id in ADMINS:
        new_user.is_admin = True
        new_user.save()
    return new_user


# Получить или создать пользователя
def get_or_create_user(id: int, name: str) -> TgUser:
    user = get_user(id)

    if user:
        return user
    return create_user(id, name)


# Получить активных пользователей
def get_active_users() -> int:
    # Выбирем кол-во пользователей, у которых дата последней активности меньше недели назад
    amount = TgUser.select().where(TgUser.last_activity > (datetime.utcnow() - timedelta(weeks=1))).count()
    return int(amount)
