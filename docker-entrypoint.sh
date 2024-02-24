#!/bin/sh

# Создаем миграции при наличии изменений в моделях
pw_migrate create --auto --database $(python3 db_url.py) --directory ./migrations Changes
# Миграция бд
pw_migrate migrate --database $(python3 db_url.py) --directory ./migrations

# Запуск бота
python3 main.py