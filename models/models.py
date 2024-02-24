from peewee import Model, ForeignKeyField, BigIntegerField, CharField, BooleanField, DateTimeField, TextField, IntegerField
from loader import psql_db


class BaseModel(Model):
    class Meta:
        database = psql_db


class TgUser(BaseModel):
    id = BigIntegerField(verbose_name="ID ключ", primary_key=True)
    name = CharField(verbose_name="Имя", null=True)
    is_admin = BooleanField(verbose_name="Админ", default=False)
    last_activity = DateTimeField(verbose_name="Последняя активность", null=True)
    created_at = DateTimeField(verbose_name="Создано", default=False, null=True)

    def __repr__(self) -> str:
        return f"<Пользователь {self.id}>"

    class Meta:
        pass


class Person(BaseModel):
    name = CharField(verbose_name="Имя", null=True)
    place = IntegerField(verbose_name="Позиция в выдаче", null=True)

    def __repr__(self) -> str:
        return f"<{self.name}>"

    class Meta:
        pass


class Title(BaseModel):
    name = CharField(verbose_name="Наименование", null=True)
    is_default = BooleanField(verbose_name="По умолчанию", default=False)
    place = IntegerField(verbose_name="Позиция в выдаче", null=True)
    tap_count = IntegerField(verbose_name="Кол-во нажатий", default=0)

    def __repr__(self) -> str:
        return f"<{self.name}>"

    class Meta:
        pass


class Photo(BaseModel):
    photo_id = CharField(verbose_name="Айди фото", null=True)

    def __repr__(self) -> str:
        return f"<{self.name}>"

    class Meta:
        pass


class Event(BaseModel):
    user = ForeignKeyField(TgUser, verbose_name="Пользователь", null=True)
    title = ForeignKeyField(Title, verbose_name="Наименование", null=True)
    is_default = BooleanField(verbose_name="По умолчанию", default=False)
    text = TextField(verbose_name="Описание", null=True)
    photo = ForeignKeyField(Photo, verbose_name="Картинка", null=True)
    person = ForeignKeyField(Person, verbose_name="Для кого", null=True)
    button_text = CharField(verbose_name="Текст кнопки", null=True)
    button_link = CharField(verbose_name="Ссылка кнопки", null=True)
    date = DateTimeField(verbose_name="Дата", null=True)
    message_date = DateTimeField(verbose_name="Дата отправки сообщения", null=True)

    def __repr__(self) -> str:
        return f"<Праздник {self.title}>"

    class Meta:
        pass
