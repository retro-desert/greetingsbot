# <p align="center">Greetings bot
<p align="center">A bot to select congratulations for your friends, relatives, etc. And also you can add your holiday to the bot and it will remind you about it in 2 days!
<br>Stack: <b>Aiogram + PostgreSQL + Celery + Redis</b>

## Quickstart
### Docker
```bash
$ git clone https://github.com/retro-desert/greetingsbot
$ cd greetingsbot
```
- Fill in the **.env** file using the example from **.env_example**
- Start bot
```bash
$ make up
```
- Fill in with default data (once!)
```bash
$ docker exec -it bot_container python3 fill_db.py
Подтверди заполнение БД ("YES"):YES
```
- Stop bot
```bash
$ make down
```
## P.S.
**This is an MVP version of the product that has not undergone any edits or refactoring**