import typing
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from data.config import ADMINS


class AdminFilter(BoundFilter):
    key = "is_admin"

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, message: Message):
        if self.is_admin is None:
            return False
        return (message.from_user.id in ADMINS) == self.is_admin
