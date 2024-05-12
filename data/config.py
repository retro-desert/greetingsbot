from decouple import config

# Инициализация переменных окружения
ADMINS = [int(_) for _ in config("ADMINS", default="").split(",")]
TOKEN = config("TOKEN")
DATABASE = config("DATABASE")
USER = config("DBUSER")
PASSWORD = config("DBPASSWORD")
HOST = config("DBHOST")
PORT = int(config("DBPORT"))
BIRTHDAY = "День Рождения"
THANKSGIVING = "День Благотворительности"
LOVE_DAY = "14 февраля - День всех влюбленных"
MARCH_8 = "8 марта – Международный женский день"
SEPTEMBER_1 = "1 сентября - День Знаний"
DECEMBER_3 = "3 декабря - Щедрый вторник"
NEW_YEAR = "31 декабря - Новый год"
JANUARY_25 = "25 января - День студента"
NEW_MEMBER = "Поздравления с пополнением в семействе"

MOTHER = "Маму"
FATHER = "Папу"
GRANDMOTHER = "Бабушку"
GRANDFATHER = "Дедушку"
FRIEND = "Друга"
GIRLFRIEND = "Подругу"
LOVER_MAN = "Мужа/любимого"
LOVER_WOMAN = "Жену/любимую"
BROTHER = "Брата"
SISTER = "Сестру"
RELATIVE = "Родственника"
COLLEAGUE = "Коллегу"
MANAGER = "Руководителя"
PET = "Питомца"
TEACHER = "Преподавателя"
STUDENT = "Студента"
SCHOOLBOY = "Школьника"

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = int(config("REDIS_PORT"))
