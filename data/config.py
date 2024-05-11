from decouple import config

# Инициализация переменных окружения
ADMINS = [int(_) for _ in config("ADMINS", default="").split(",")]
TOKEN = config("TOKEN")
DATABASE = config("DATABASE")
USER = config("DBUSER")
PASSWORD = config("DBPASSWORD")
HOST = config("DBHOST")
PORT = int(config("DBPORT"))
MEN_LIST = ("Папу", "Дедушку", "Брата", "Друга", "Родственника", "Мужа/любимого")
WOMEN_TITLE = ("8 марта – Международный женский день")
SEPTEMBER_1ST_TITLE = "1 сентября - День Знаний"
NOT_SEPTEMBER_LIST = ("Родственника", "Коллегу", "Руководителя", "Питомца")
REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = int(config("REDIS_PORT"))
