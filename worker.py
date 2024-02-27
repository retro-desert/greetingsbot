import asyncio
from celery import Celery
from celery.utils.log import get_task_logger
from datetime import datetime, timedelta
from data.config import REDIS_HOST, REDIS_PORT
from bot.services import get_user
from loader import disp
from models import Event

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

celery_event_loop = asyncio.new_event_loop()

app = Celery("celery", broker=CELERY_BROKER_URL)
app.autodiscover_tasks()
logger = get_task_logger(__name__)

app.conf.beat_schedule = {
	"check_task": {
		"task": "check_task",
		"schedule": 60 * 5,
		"args": (),
	},
}


async def send_notify(event: dict) -> bool:
	user = get_user(event["user"])
	text = f"Напоминаем вам о важном событии - {event['text']}\nДата: {event['date']}\nСкорее выберите поздравление.\n\nЦелуем, фонд Соломон"
	await disp.bot.send_message(user.id, text)
	return True


async def check_events() -> bool:
	now = datetime.utcnow()
	events = Event.select(
		Event.id,
		Event.user,
		Event.date,
		Event.text,
		Event.message_date).where(
		Event.is_default == False,
	).dicts()

	for i in events:
		event_date = i["date"].replace(year=now.year)
		if -2 <= int((now - event_date).days) <= 0:
			if i["message_date"]:
				if i["message_date"] + timedelta(days=30) > now:
					break
			if await send_notify(event=i):
				obj = Event.get(Event.id == i["id"])
				obj.message_date = now
				obj.save()
	return True


@app.task(name="check_task", max_retries=3, default_retry_delay=5)
def check_task() -> None:
	try:
		celery_event_loop.run_until_complete(check_events())
	except Exception as e:
		logger.error(f"[check_task] Ошибка: {str(e)}")