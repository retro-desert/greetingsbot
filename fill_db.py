# Стандартные праздники
from models import Event, Person, Title, Photo

default_events = (
	"14 февраля - День всех влюбленных",
	"8 марта – Международный женский день",
	"1 сентября - День Знаний",
	"5 сентября - Международный день Благотворительности",
	"3 декабря - Щедрый вторник",
	"31 декабря - Новый год",
	"25 января - День студента",
	"День Рождения близкого человека"
)

persons = (
	"Поздравления для Мамы",
	"Поздравления для Папы",
	"Поздравления для Бабушки",
	"Поздравление для Дедушки",
	"Поздравление для Брата",
	"Поздравление для Сестры",
	"Поздравление для Любимого мужчины",
	"Поздравление для Любимой девушки",
	"Поздравление для родственника",
	"Поздравление для Коллеги",
	"Поздравления для Руководителя",
	"Поздравления для питомца"
)

greetings = {
	"00": [
		{
			"text": "Мама, ты – моя настоящая любовь! Спасибо за бесконечное терпение и нежность. С Днём Святого Валентина!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Мамочка, поздравляю тебя с Днём Святого Валентина! Твои ласковые слова и забота делают каждый мой день особенным.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Дорогая мама, с Днём Святого Валентина! Наши сердца бьются в унисон - люблю тебя!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Поздравляю тебя, моя самая родная мамочка, с Днём Святого Валентина! Скучаю по тебе сильно, обнимаю тебя крепко, люблю тебя нежно!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Милая мама, с Днём Святого Валентина! Пусть огонь нашей любви горит ещё ярче!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"01": [
		{
			"text": "Пап, сердечно поздравляю тебя в этот любвеобильный день! Твои советы и поддержка – для меня бесценны.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С любовью и благословением в День Святого Валентина для самого заботливого и мудрого папы. Ты – настоящий герой!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Папочка, поздравляю тебя с Днём Святого Валентина! Твоя помощь и забота делают каждый день удачным и ярким.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Папа, привет! День Святого Валентина пришёл) Твоя сила и мудрость – моё вдохновение.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Дорогой папа, с Днём Святого Валентина! Твоя любовь – как крепкий фундамент, на котором строится моя жизнь.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},

	],
	"02": [
		{
			"text": "Дорогая бабушка, с Днём Святого Валентина! Твоя любовь – как самый мягкий и теплый плед в холодные дни.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Бабушка, с любовью и благословением в этот особенный день! Твои советы и забота  – для меня самое ценное сокровище.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Дорогая бабушка, с Днём Святого Валентина! Твоя любовь – как светлячок, озаряющий мой путь.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Бабушка, в этот день любви и тепла, хочу сказать тебе, как я тебя люблю! С Днём Святого Валентина!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С Днём Святого Валентина, любимая бабушка! Ты – мой образец доброты и мудрости, я тобой горжусь.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"03": [
		{
			"text": "Дорогой дедушка, с Днём Святого Валентина! Твоя любовь – как тёплое солнце, согревающее моё сердце.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Дедушка, с любовью и уважением в этот особенный день! Твоя мудрость и стойкость – для меня вечный источник вдохновения.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Поздравляю тебя, мой самый заботливый дедушка, с Днём Святого Валентина! Твои советы – мой надёжный компас в жизни.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Дедушка, в этот день хочу сказать тебе, как я тебя ценю и люблю! С Днём Святого Валентина!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С Днём Святого Валентина, дедушка! Ты – мой герой и учитель, я тобой горжусь.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"04": [
		{
			"text": "Братишка, с Днём Святого Валентина! Твоя поддержка и дружба – для меня как спасательный круг в океане жизни.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Брат, с любовью и благословением в этот особенный день! Твоя сила и решимость всегда меня вдохновляют.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Дорогой брат, с Днём Святого Валентина! Твоя весёлая натура и доброе сердце делают каждый день особенным.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Брат, с Днём Святого Валентина! Твоя заразительная улыбка – мой источник радости и оптимизма.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С тобой всегда весело, брат! С Днём Святого Валентина! Твоя жизнерадостность – мое бесценное богатство.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"05": [
		{
			"text": "Сестрёнка, с Днём Святого Валентина! Твоя забота и нежность – как лучики солнца в моей жизни.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Дорогая сестричка, с любовью и благословением в этот особенный день! Твоя умная голова и доброе сердце – радость моих дней.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Сердечно поздравляю самую лучшую сестру с Днём Святого Валентина! Твоя поддержка – мой надёжный причал.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Сестричка, с Днём Святого Валентина! Твоя улыбка и веселый настрой делают каждый момент весёлым и особенным.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Дорогая сестра, с Днём Святого Валентина! Твоя открытость и чувство юмора радуют моё сердце!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"06": [
		{
			"text": "Мой дорогой, с Днём Святого Валентина! Твоя любовь – моё счастье! Ты вдохновляешь меня.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Любимый, моё сердечко бьётся чаще, когда ты рядом! С Днём Святого Валентина, дорогой!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С любовью и страстью поздравляю тебя, мой герой, с Днём Святого Валентина! Твоя ласка и забота – моя радость.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Любимый мой, поздравляю тебя с Днём Святого Валентина! Быть в твоих  объятиях – любимое занятие!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Дорогой, с Днём Святого Валентина! Ты отогрел моё сердце и душу, я счастлива!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"07": [
		{
			"text": "Моя дорогая, с Днём Святого Валентина! Твоя нежность и красота – мой источник восторга и вдохновения.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С любовью и страстью поздравляю тебя, моя прекрасная, с Днём Святого Валентина! Твоя улыбка делает любой день солнечным!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Моя дорогая, с Днём Святого Валентина! Твоя ласка и забота – как тёплый весенний ветер.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С тобой каждый момент полон любви, милая. С Днём Святого Валентина! Твоя светлая голова и любящее сердце – моё вдохновение.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Любимая, с любовью и страстью в этот день! Ты – мой райский сад и источник радости.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"08": [
		{
			"text": "С Днём Святого Валентина, родной(ая)! Твоя мудрость – мой самый надежный компас.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С Днём Святого Валентина, родной(ая)! Твоя улыбка – это солнце, согревающее наши сердца.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Родственник(ца) мой(моя), с любовью и благословением в этот особенный день! Твоя поддержка – мое убежище.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С Днём Святого Валентина, дорогой(ая) родственник(ца)! Твоя дружба – высшая ценность.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Родной(ая), с любовью и теплом в этот особенный день! Твоя забота – как летний дождь, питающий корни нашей семейной любви.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"09": [
		{
			"text": "Уважаемый(ая) коллега, с Днём Святого Валентина! Твой профессионализм и отзывчивость – пример для подражания.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С Днём Святого Валентина, уважаемый(ая) коллега! Твоя трудовая активность и ответственность вдохновляют нашу команду.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Коллега, с любовью к профессии и благодарностью за твою отличную работу! С Днём Святого Валентина!",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Уважаемый(ая) коллега, с Днём Святого Валентина! Твоя инициатива и умение решать нестандартные задачи впечатляют.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С Днём Святого Валентина, уважаемый(ая) коллега! Твои идеи и креативный подход делают наши проекты уникальными.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"010": [
		{
			"text": "С благодарностью и уважением поздравляю вас, руководитель(ница), с Днём Святого Валентина! Ваши организаторские способности окрыляют и зовут на трудовые подвиги.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Руководитель(ница), с любовью к работе и уважением к сотрудникам! С Днём Святого Валентина! Ваша лидерские качества вдохновляют на новые достижения.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Уважаемый(ая) руководитель(ница), с Днем Святого Валентина! Ваше внимание к деталям и стремление к совершенству – наша гордость.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Руководитель(ница), с Днём Святого Валентина! Ваша способность мотивировать – наше секретное оружие.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С благодарностью за ваши трудовые усилия, руководитель(ница)! С Днём Святого Валентина! Ваша справедливость и мудрость –  наша верная опора.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"011": [
		{
			"text": "Мой дорогой пушистик (или кличка питомца), с Днём Святого Валентина! Твои ласки и верность – моя истинная радость.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С любовью и теплом поздравляю моего верного друга с Днём Святого Валентина! Твои ласковые мурчания делают мою жизнь яркой.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Поздравляю тебя, мой пушистик (или кличка питомца), с Днём Святого Валентина! Твоя преданность – моё главное сокровище.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "Мой милый друг, с Днём Святого Валентина! Твои нежные прикосновения дарят мне настоящий уют.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
		{
			"text": "С праздником, мой хвостатый друг! Твои весёлые выходки – моё непередаваемое счастье.",
			"photo_id": "AgACAgIAAxkBAAPyZcfIz1y8PXkb9oPNCNr9phUde9YAAobZMRtqZtFJM10NozIiLuwBAAMCAAN3AAM0BA"
		},
	],
	"10": [
		{
			"text": "Мам, с 8 марта! Твоя суперсила – как у настоящей супергероини! Ты мегамама!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая мама, с Международным женским днём тебя! Пусть твои выходные будут такими же волшебными, как ты!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": 'Мамочка, с 8 марта! Ты – наш главный "шеф-повар" и чемпион по наведению порядка!',
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, мама! Ты – наша любимая командирша в битве за семейное благополучие!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Мамуля, с 8 марта! Ты – настоящая звезда нашего семейного шоу!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"11": [
		{
			"text": "Папа, с 8 марта! Ты большой молодец и пример для подражания!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": 'Дорогой папочка, 8 марта - праздник для всех, а не только для женщин! Ты – наш непревзойденный мастер по "ремонту" и "сборке" счастья.',
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": 'Пап, с 8 марта! Твои заботы – как настоящий "кредит" любви и уюта в нашей жизни.',
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": 'С праздником, папа! Ты – наш незаменимый и главный "проводник" по жизненному пути.',
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Папуля, с 8 марта! Твоя забота – как страховка, надежно покрывающая все семейные риски!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"12": [
		{
			"text": "Бабушка, с 8 марта! Твои советы –  золото - их ценность только растёт!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая бабушка, с Международным женским днём тебя! Твои кулинарные шедевры – достойны самой высокой оценки!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Бабуля, с восьмым марта! Твоя мудрость – как луч света в наших семейных тоннелях)",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": 'С праздником, бабушка! Ты – наша главная "колдунья", превращаешь обыденные моменты в волшебные.',
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Любимая бабушка, с 8 марта! Твой стиль и элегантность вне времени!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"13": [
		{
			"text": "Дедушка, с 8 марта! Твои истории словно машина времени. Спасибо за волшебные путешествия в прошлое!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": 'Дорогой дедушка, с Международным женским днём тебя! Твои советы – это "инвестиции" в успешное семейное будущее.',
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Дедуля, с 8 марта! Ты настоящий супергерой нашей семьи!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": 'С праздником, дедушка! Ты – наш главный "мастер по ремонту" любых жизненных поломок.',
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Любимый дедушка, с 8 марта! Твоя доброта – как солнце, освещающее наш семейный путь!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"14": [
		{
			"text": "Братишка, с 8 марта! Твои шутки – заряд положительной энергии для всей семьи!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": 'С 8 марта, брат! Ты – наш главный "зачинщик" веселья.',
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Брат, с Международным женским днём тебя! Твои кулинарные эксперименты – настоящее искусство!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Поздравляю тебя, братик, с 8 марта! Твоя главная сила в добром сердце.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Брат, с праздником! Твоя ослепительная улыбка – как солнечный лучик, сразу становится тепло!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"15": [
		{
			"text": "Сестричка, с 8 марта! Твои советы – как мультитул в нашем семейном ящике с инструментами.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая сестра, с Международным женским днём тебя! Твои кулинарные эксперименты – наше любимое гастрономическое приключение!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Сестрёнка, с 8 марта! Твоя энергия – как магнит, притягивающий позитив и радость.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Поздравляю тебя, сестрица, с 8 марта! Твоя сила – в твоей уникальности.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Сестра, с праздником! Твоя доброта – как волшебная палочка, делающая наш мир ярче.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"16": [
		{
			"text": "Мой дорогой, с 8 марта! Твоя любовь – как тёплый ветерок, уносящий все заботы.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С любовью и праздником, мой герой! Твои поступки – как главные главы в нашей истории любви.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Любимый, с 8 марта! Твоя защита – как крепкая стена, ограждающая от невзгод.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Поздравляю с Международным женским днём, дорогой мой человек! Твоя забота – мой главный источник счастья.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Милый, с праздником! Ты – мой особенный повод для улыбок каждый день.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"17": [
		{
			"text": "Моя любовь, с 8 марта! Твоя красота – магическое сияние, освещающее мою жизнь ярче солнца.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, моя прекрасная! Твои лучезарные улыбки – радость моих глаз!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая, с восьмым марта! Твоя нежность делает меня счастливым!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С Международным женским днём тебя, моя ненаглядная! Твоя поддержка вдохновляет на новые свершения!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Милая, с праздником! Ты –  бриллиант моего сердца и услада моих глаз!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"18": [
		{
			"text": "Дорогой родственник, с 8 марта! Твоя отзывчивость и общительность объединяют всю семью.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С 8 марта, родной! Твои дельные советы – лучше любого навигатора.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Родственник, с Международным женским днём тебя! Твоя помощь всегда приходит вовремя.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, близкий родственник! Твоя доброта – лучший пример для всех нас.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Родной, с 8 марта! Ты играешь очень важную роль в нашем семейном «кино»!",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"19": [
		{
			"text": "Коллега, с 8 марта! Твой профессионализм – как бриллиант в короне нашей команды.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С Международным женским днём тебя, коллега! Твои идеи – как вишенка на торте нашего проекта.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Коллега, с 8 марта! Ты настоящий командный игрок – в положительном результате всегда есть твоя заслуга.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, дорогая коллега! Твоя энергия вдохновляет всех нас.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Коллега, с 8 марта! Твоя добродушная улыбка – как витаминка для тонуса в офисе.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"110": [
		{
			"text": "Уважаемый руководитель, с 8 марта! Для нас вы маяк, указывающий путь к успеху.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С Международным женским днём, уважаемый начальник! Ваше руководство – гарантия нашего общего успеха.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Руководитель, с 8 марта! Ваше лидерство – как факел, освещающий наш трудовой путь.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, уважаемый руководитель! Ваша поддержка помогает достигать целей.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Руководитель, с 8 марта! Ваш профессионализм – как надёжный  двигатель, что обеспечивает поступательный рост к новым вершинам.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"111": [
		{
			"text": "Мой милый пушистик (или кличка), с 8 марта! Твои мурчания – лучшая музыка для моих ушей.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, моя пушистая радость! Твои весёлые игры отвлекают от забот и не дают скучать.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Питомец, с 8 марта! Твоя преданность – настоящая драгоценность моей жизни.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "С Международным женским днём, мой четвероногий друг! Твоя ласка – как исцеляющий бальзам для моей души.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
		{
			"text": "Мой любимчик, с праздником! Твои шалости – как радуга в серых буднях моей жизни.",
			"photo_id": "AgACAgIAAxkBAAIBimXJA6wsYqN9RlW7RJtdcajXY79gAAKY0jEbDkJISpj6LdR1SxLHAQADAgADdwADNAQ"
		},
	],
	"20": [
		{
			"text": 'Мам, с 1 сентября! Надеюсь, в этом "учебном году" ты не опоздаешь на наши встречи и обеды!',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая мама, с Днем Возвращения в Режим! Поднимай настроение, как будто поднимаешь пульс на физкультуре.",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Мамочка, с праздником! Пусть этот "школьный год" принесет тебе отличные оценки в категории "Домашний миротворец".',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Мама, календарь перевернули и снова 1 сентября. Ты сильная, ты справишься - поздравляю с началом нашего общего учебного года!",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Мамуля, с 1 сентября тебя! Пусть День знаний принесёт тебе только приятные эмоции!",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"21": [
		{
			"text": 'Папа, с 1 сентября! Надеюсь, ты готов к "урокам" по выживанию в семье!',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Дорогой папочка, с Днем Возвращения в "Школу Жизни"! Пусть наше семейное коворкинг-пространство будет весьма успешным.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Папуля, с праздником! Пусть каждый домашний эксперимент принесет тебе заслуженную награду.",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Пап, тебя в школу вызывают - с цветами! 1 сентября на дворе - да будет праздник! ",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Папа, наступил День знаний! Поздравляю тебя и торжественно обещаю - учиться, учиться и ещё раз учиться)",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"22": [
		{
			"text": 'Бабушка, с 1 сентября! В этом "учебном году" ждем от тебя уроки "Секреты Волшебной Кулинарии"!',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Дорогая бабушка, с Днем Возвращения к "Учебнику Жизни"! Твои истории – лучший урок для понимания семейных традиций.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Бабушка, с праздником! Пусть этот "школьный год" принесет тебе только смех и радость.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Бабуля, сегодня красный день календаря - День знаний! Ты всегда говорила, что знания - сила, пусть новый учебный год придаст сил всем нам.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Бабушка, с 1 сентября тебя! Новый учебный год это хорошо забытый старый) Будем делать домашние задания вместе?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"23": [
		{
			"text": 'Дедушка, с 1 сентября! Готов ли ты к "урокам по возвращению в детство" с внуками?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Дорогой дедушка, с Днем Возвращения к "Школе Веселья"! Твои уроки юмора – наш фирменный стиль.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Дедуля, с праздником! Пусть этот "школьный год" принесет тебе невероятные приключения с нашими весёлыми внуками.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Дедушка, на дворе опять 1 сентября - начинается новый учебный сезон. Без твоего опыта и знаний нам не обойтись!",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Дедушка, на нас опять наступает 1 сентября. Спасибо, что словом и делом помогаешь в нелёгком деле обучения.",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"24": [
		{
			"text": 'Братишка, с 1 сентября! Готов ли ты к "школьным заметкам" о том, как ты занимаешь ванную вечером?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Брат, с Днем Возвращения к "Школе Братства"! Ты – мой личный гуру по семейным приключениям.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Братик, с праздником! Пусть этот "школьный год" принесёт нам новые рекорды по придумыванию весёлых прозвищ.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Брат мой, крепись - впереди новый учебный год. Мы будем вместе в нашей борьбе за знания!",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Брат, 1 сентября надвигается! Ты ведь поможешь мне с домашкой, правда?",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"25": [
		{
			"text": 'Сестричка, с 1 сентября! Готова ли ты к "урокам женской магии" в этом семейном учебном году?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Дорогая сестра, с Днем Возвращения к "Школе Женственности"! Твои лайфхаки – неотъемлемая часть нашего семейного арсенала.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Сестренка, с праздником! Пусть этот "школьный год" принесет нам невероятные сюрпризы и весёлые моменты.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Сестрица, привет! У нас опять 1 сентября - давай праздновать, уроки только завтра)",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Сестра, этот день настал. Школы опять открыли свои двери и ждут учеников. Мы выдержим это и будем гордиться собой.",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"26": [
		{
			"text": 'Мой любимый, с 1 сентября! Надеюсь, ты готов к "урокам семейной гармонии" с любовью и уважением!',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'С Днём знаний, мой герой! Пусть этот "школьный год" будет наполнен яркими моментами и нежными объятиями.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Любимый, с Днем Возвращения к "Школе Любви"! Ты – моё любимое учебное пособие, буду изучать тебя досконально)',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой, с 1 сентября тебя! Я буду самой прилежной ученицей!",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Милый мой, вот и лето прошло - 1 сентября. Давай выучим что-нибудь новенькое вместе!",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"27": [
		{
			"text": 'Моя любовь, с 1 сентября! Готова ли ты к "урокам нежности" и "заданиям по расцветанию от счастья"?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'С любовью и праздником, моя прекрасная! Пусть этот "школьный год" будет полон цветов и улыбок.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Дорогая, с Днем Возвращения к "Урокам Романтики"! Твои поцелуи – лучшее начало учебного дня.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Поздравляю с Днём знаний, умничка! Цветы будут не только 1 сентября - обещаю!",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Знание - сила, дорогуша! С 1 сентября тебя - будем учить друг друга уму-разуму)",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"28": [
		{
			"text": 'Дорогой родственник, с 1 сентября! Готов ли ты к "урокам семейных тайн" и "традиций празднования"?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'С возвращением в "Школу Родных"! Пусть этот год принесет нам множество семейных встреч и теплых моментов.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Родной, с праздником! Пусть наши семейные уроки будут веселыми и полезными.",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Привет, родня! С 1 сентября тебя! Учение - свет, да будет свет!",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Родственная душа, с Днём знаний тебя! Будем учиться и обязательно научимся.",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"29": [
		{
			"text": 'Коллега, с 1 сентября! Готов ли ты к "урокам корпоративной этики" и "мистическим исчезновениям из офиса"?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'С возвращением в "Школу Офисных Приключений"! Пусть этот год принесет нам меньше срочных заданий и больше чайных пауз.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Коллега, с праздником! Пусть наши совместные "школьные проекты" будут успешными и весёлыми.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Коворкер, поздравляю с Днём знаний! Учиться никогда не поздно, поэтому начнём завтра)",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой мой сослуживец! Поздравляю с началом нового учебного года! Успехов в учёбе и изучении.",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"210": [
		{
			"text": 'Уважаемый руководитель, с 1 сентября! Готов ли ты к "урокам лидерства" и "творческому вдохновению"?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'С возвращением в "Школу Руководства"! Пусть этот год принесет вам меньше репетиторов и больше идей от нашей креативной команды.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Руководитель, с праздником! Пусть этот "учебный год" принесет вам много успешных проектов и свежих идей.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём знаний, босс! Будем учиться новому и расти над собой под вашим чутким руководством.",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой наш начальник! С 1 сентября! Вы наш учитель, а мы прилежные ученики - впереди общий успех",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"211": [
		{
			"text": 'Мой милый пушистик (или кличка), с 1 сентября! Готов ли ты к "урокам игривости" и "мастер-классам по уюту"?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'С возвращением в "Школу Котейки"! Пусть этот год принесет тебе больше игрушек и чесаний за ушком.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": "Питомец, с праздником! Пусть уроки прыжков и гуляний будут освоены на отлично.",
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'Мой хвостатый друг, с 1 сентября! Готов ли ты к "урокам дружбы" и "ловкости на лапках" в этом сезоне?',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
		{
			"text": 'С возвращением в "Школу Пушистости"! Пусть этот год принесет тебе много новых игрушек, весёлых приключений и вкусных лакомств.',
			"photo_id": "AgACAgIAAxkBAAIB12XJCFd9wFyuLyCCj_5dFV4aJiEgAALP0jEbDkJISmEUmqTCi4mVAQADAgADdwADNAQ"
		},
	],
	"50": [
		{
			"text": "Мам, с наступающим Новым Годом! Пусть твои рецепты семейного счастья  будут такими же волшебными, как твои кулинарные шедевры!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая мамочка, с Новым Годом! Твоя любовь делает нас счастливыми!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Мама, с праздником! Просто будь собой и не переживай по пустякам - у нас всё получится!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С наступающим, мама! Береги себя, будь умничкой - мы вместе, значит всё будет хорошо!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Мамуля, с Новым Годом! Пусть наши семейные посиделки случаются чаще. Для счастья не нужен повод.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"51": [
		{
			"text": "Пап, с наступающим Новым Годом! Пусть твои забавные истории не кончаются, а бюджет выдержит «подарочную» нагрузку!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой папочка, с Новым Годом! С нетерпением ждём твоих новых кулинарных экспериментом!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Папа, с праздником! Пусть наступающий год принесет тебе не только хорошую погоду для барбекю, но и больше времени для семейного шопинга.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": 'С наступающим, папа! Пусть новый год станет для тебя поводом открыть новую страницу в своем "блоге отца" с еще более креативными советами.',
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Папуля, с Новым Годом! Пусть наши семейные поединки в компьютерных играх будут такими же захватывающими, как и твои звёздные стратегии на работе!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"52": [
		{
			"text": "Бабушка, с наступающим Новым Годом! Твоё вязание в 100 раз выше любой высокой моды.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая бабушка, с Новым Годом! Будь счастлива, не болей и почаще радуй своей стряпнёй!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Бабуля, с праздником! Пусть новый год принесет тебе побольше солнечных дней на даче!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": 'С наступающим, бабушка! Ты замечательно читаешь внукам сказки перед сном, а как насчёт собственной  книги "Мемуары Гиперактивной Бабушки"?',
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Любимая бабушка, с Новым Годом! Пусть наши встречи будут такими же теплыми, как твои пледы, и такими же  вдохновляющими, как твои рассказы о своих приключениях!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"53": [
		{
			"text": "Дедушка, с наступающим Новым Годом! Пусть в новом году ты продолжишь удивлять своими историями, с годами они становятся только интереснее.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой дедушка, с Новым Годом! Твой опыт и оптимизм заряжает нас положительной энергией.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Дедуля, с праздником! Желаю побольше тёплых дней и увлекательных путешествий на дачу и не только)",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С наступающим, дедушка! В новом году ты научишь нас играть в шахматы, а мы поможем освоить смартфон - идёт?",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Любимый дедушка, с Новым Годом! План такой: болеть меньше, двигаться больше и ежедневно радоваться жизни. Приступаем немедленно!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"54": [
		{
			"text": "Братишка, с наступающим Новым Годом! Пусть этот год принесет тебе не только новые рекорды в видеоиграх, но и успехи на работе.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Брат, с Новым Годом! Желаю новых рекордов в фитнес-клубе, на стадионе и на спортплощадке!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": 'С праздником, бро! Надеюсь, что  этот год принесет тебе не только признание на работе, но и победу в семейных "спортивных дуэлях".',
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С наступающим, брат! Пусть в новом году будет больше креатива и творчества.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": 'Братишка, с Новым Годом! Пусть наши "бои" за пульт от телевизора будут такими же зрелищными, как чемпионаты по футболу!',
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"55": [
		{
			"text": "Сестричка, с наступающим Новым Годом! Желаю твоим мечтам сбываться! Будь здорова и счастлива, как никогда прежде!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая сестра, с Новым Годом! Увлекайся и увлекай, радуйся и радуй, удивляйся и удивляй! Люблю тебя!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Сестренка, с праздником! Пусть этот год принесёт тебе не только успехи в работе, но и безудержное веселье в кругу семьи.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С наступающим, сестричка! Пусть новый год станет для тебя поводом открыть новые горизонты в путешествиях и увлекательных занятиях.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая сестра, с Новым Годом! Пусть наши семейные вечера будут такими же теплыми, как и твои объятия, и такими же весёлыми, как твои шутки!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"56": [
		{
			"text": 'Мой любимый, с наступающим Новым Годом! Пусть этот год принесёт нам не только романтические встречи, но и множество "боев" в мире видеоигр.',
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С любовью и праздником, мой герой! Пусть новый год будет для нас таким же захватывающим, как и твои спасательные операции в нашей домашней обители.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Любимый, с Новым Годом! Давай будем делать друг друга лучше и развиваться вместе.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С наступающим, милый! Пусть новый год принесёт тебе не только успехи в работе, но и больше времени для наших совместных приключений.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Мой дорогой, с Новым Годом! Пусть каждый день в нашей жизни будет таким же запоминающимся, как твои невероятные сюрпризы! Ты потрясающий!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"57": [
		{
			"text": "Дорогая, с Новым Годом! Желаю нашим отношениям быть такими же красочными, как фейерверки в ночном небе.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С Новым Годом, моя любовь! Пусть в новом  году не будет места для скуки - давай веселиться и смеяться! Жизнь проще, чем кажется.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, моя прекрасная! Пусть наши отношения в новом году будут такими же яркими, как нарядная ёлка.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Любимая, с Новым Годом! Хочу, чтобы каждый день был полон радости, улыбок и невероятных сюрпризов!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Моя драгоценная, с Новым Годом! Пусть наша любовь будет крепкой, как самогон твоего папы)",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"58": [
		{
			"text": "Родной/родная, с Новым Годом! Пусть этот год будет таким же удивительным, как разговоры, которые мы ведём в кругу семьи.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С Новым Годом, родственник! Пусть в этом году наши семейные собрания будут такими же шумными и весёлыми, как салют в полночь.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, родня! Пусть каждый момент с вами будет таким же согревающим, как чашка горячего чая в морозный вечер.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогие родственники, с Новым Годом! Удачи, любви и терпения всем нам.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Родные мои, с Новым Годом! Желаю оставаться собой, помогать друг другу и чаще встречаться вне сети.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"59": [
		{
			"text": "Коллега, с Новым Годом! Пусть в нашем офисе будет столько же вкусного, сколько в праздничном салате!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С Новым Годом, коллеги! Желаю щёлкать рабочие задачи как орешки. Орешки с варёной сгущёнкой, конечно)",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, уважаемые коллеги! Любая цель будет нам по плечу, если коллектив сплотится. И для начала плотненько закусим)",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Коллеги, с Новым Годом! Пусть наша команда будет такой же согласованной, как огоньки на гирлянде.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Уважаемые сотрудники, с Новым Годом! Пусть в этом году в нашем офисе будет столько же хороших идей, сколько игрушек на ёлке.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"510": [
		{
			"text": "Уважаемый руководитель, с Новым Годом! Пусть в этом году наши проекты будут такими же успешными, как ваша стратегия управления.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С Новым Годом, уважаемый начальник! Пусть в нашем подразделении будет столько же вдохновения, сколько в ваших мотивационных речах.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, руководитель! Впереди Новый год и новые свершения, команда готова и ждёт ваших указаний.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С Новым Годом, босс! Пусть наши корпоративные цели будут достигнуты так же быстро, как летит пробка из бутылки.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Руководитель, с Новым Годом! Ваша мудрость в паре с нашей исполнительностью сделают реальностью самые смелые мечты!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"511": [
		{
			"text": "Мой пушистик (или кличка), с Новым Годом! Пусть этот год будет полон новых игрушек, вкусняшек и прогулок.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "С Новым Годом, мой четвероногий друг! Ты образец позитивного настроения и увлечённости!",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Милый питомец, с праздником! Пусть новогодние угощения будут вкусными, как твои любимые лакомства.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Пушистик, с Новым Годом! Пусть каждый день будет наполнен игрой, уютом и лаской.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
		{
			"text": "Любимец, с Новым Годом! Ты настоящий друг и неповторимый комочек счастья, не болей и не грусти, когда меня нет рядом.",
			"photo_id": "AgACAgIAAxkBAAIB2WXJDA-Qv8jlToQFE-QCxSdxIzKEAALj0jEbDkJISsaN61k1EOu3AQADAgADdwADNAQ"
		},
	],
	"70": [
		{
			"text": "Мам, с Днём Рождения! Ты всегда молодая и стильная, даже когда пытаешься понять, как пользоваться смайликами в сообщениях!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая мамочка, с праздником! Пусть этот год будет таким же увлекательным, как твои попытки разобраться в мире социальных сетей.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Рождения, мама! Обязательно помогу тебе выучить все современные мемы!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Мамуля, с праздником! Наслаждайся жизнью, радуй нас своим вниманием и не унывай - всё будет хорошо!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Мам, с Днём Рождения! Дуй на свечи, загадывай желания, радуйся каждому дню - впереди ещё много интересного!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"71": [
		{
			"text": "Пап, с Днём Рождения! Поздравляю тебя с тем, что ты такой же молодой, как и твои анекдоты, которые мы слышим каждый год)",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой папочка, с праздником! Пусть этот день будет столь же запоминающимся, как твои шутки в семейных чатах.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Рождения, папа! Поздравляю тебя с тем, что ты всегда такой весёлый, даже когда пытаешься настроить технику.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Папуля, с праздником! Пусть этот год будет полон смеха, как и твои попытки научиться использовать новые приложения на телефоне.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Пап, с Днём Рождения! Оставайся собой, празднуй весело, будь самым нарядным - это твой день!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"72": [
		{
			"text": "Бабушка, с Днём Рождения! Поздравляю тебя с тем, что ты такая же мудрая, как и твои советы, которые мы любим слушать каждый раз.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая бабушка, с праздником! Пусть этот год будет таким же теплым, как твои объятия, когда мы приходим в гости.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Рождения, бабушка! Поздравляю тебя с тем, что ты ничего не забываешь, особенно истории из детства.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": 'Бабуля, с праздником! Пусть твой день будет столь же сладким, как твои превосходные пироги.',
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Бабушка, с Днём Рождения! Мы любим тебя, ценим и очень скучаем! Ты почётный хранитель нашей семейной мудрости.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"73": [
		{
			"text": "Дедушка, с Днём Рождения! Поздравляю тебя с тем, что ты такой же обстоятельный, как твои рассказы о прежних временах.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой дедушка, с праздником! Пусть этот год будет таким же весёлым, как  твои анекдоты.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Рождения, дедуля! Поздравляю тебя с тем, что ты всегда такой добрый, как и твои советы о жизни.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дедушка, с праздником! Пусть этот день будет столь же активным, как твои прогулки по парку каждый утро.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой дед, с Днём Рождения! Поздравляю тебя с тем, что ты всё такой же крепкий, как твои объятия.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"74": [
		{
			"text": "Братан, с Днём Рождения! Поздравляю тебя с тем, что ты такой же крутой, как твои попытки выучить новый трюк на скейтборде.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой брат, с праздником! Пусть этот год будет таким же интересным, как и твои истории о приключениях.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Рождения, братишка! Поздравляю тебя с тем, что ты всегда такой же невероятно смешной, как твои шутки и розыгрыши.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": 'Братуля, с праздником! Пусть твой день будет столь же удачным, как твои попытки сделать "селфи" на каждой вечеринке.',
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Братиша, с Днем Рождения! Поздравляю тебя с тем, что ты такой же нужный, как твои советы в сложных ситуациях.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"75": [
		{
			"text": "Сестричка, с Днём Рождения! Поздравляю тебя с тем, что ты такая же красивая, как твои фотографии в соцсетях.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая сестрёнка, с праздником! Пусть этот год будет таким же волшебным, как твои идеи для оформления комнаты.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Рождения, сестричка! Поздравляю тебя с тем, что ты всегда такая же дружелюбная, как твои сообщения с утра.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Сестрёнка, с праздником! Пусть твой день будет столь же весёлым, как твои попытки научить меня танцевать.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Сестрёнка, с Днем Рождения! Люблю тебя сильно-сильно! Ты замечательная!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"76": [
		{
			"text": "Мой герой, с Днём Рождения! Хочу поскорее оказаться в твоих объятиях! Ты сильный, добрый и красивый!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Любимый, с праздником! Пусть этот год будет таким же захватывающим, как твои планы на будущее.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Рождения, мой красавчик! Поздравляю тебя с тем, что ты всегда такой внимательный и заботливый!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Мой дорогой, с праздником! Пусть твой день будет столь же стильным, как твои образы на наших совместных фотографиях.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Любимый мужчина, с Днём Рождения! Поздравляю тебя с тем, что ты такой же романтичный, как в день нашего знакомства.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"77": [
		{
			"text": "Любовь моя, с Днём Рождения! Ты восхитительна, твоя улыбка делает меня счастливым!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Любимая, с праздником! Пусть этот год будет таким же чудесным, как твои глаза, когда ты видишь подарок.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Рождения, моя прекрасная! Поздравляю тебя с тем, что ты всегда такая же позитивная, как твои мотивационные речи.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Моя дорогая, с праздником! Пусть этот день будет столь же приятным, как наши вечера вдвоём.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Любимая девочка, с Днём Рождения! Ты моё счастье, моя радость, мой стимул - эти чувства окрыляют!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"78": [
		{
			"text": "Дорогой родственник, с Днём Рождения! Поздравляю тебя с тем, что ты такой же весёлый, как наши семейные встречи.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днем Рождения, родной/родная! Пусть этот год будет наполнен только приятными и интересными событиями.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С днём варенья, родственник! Надо чаще встречаться, чтобы было что вспомнить)",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Родной/родная, с Днём Рождения! Пусть этот день будет столь же тёплым, как наши семейные ужины.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой родственник, с днём рождения! Поздравляю тебя сердечно - пусть всё будет так как ты захочешь!",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"79": [
		{
			"text": "С Днем Рождения, коллега! Надеюсь, твои рабочие проекты будут такими же успешными, как попытки скрыться от шефа в курилке)",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Коллега, с Днем Рождения! Пусть в этот год у нас будет столько же смешных моментов в офисе, сколько неудачных попыток перекусить в зоне видимости веб-камеры.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, коллега! Пусть в этот год твоя продуктивность будет такой же высокой, как уровень кофеина в наших чашках.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Коллега, с Днём Рождения! Пусть этот год принесет тебе не только профессиональный успех, но и новые рекорды по количеству мемов в нашем чате.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой коллега, с праздником! Пусть твои рабочие идеи будут такими же яркими, как твои выкрутасы на корпоративах)",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"710": [
		{
			"text": "Уважаемый руководитель, с Днём Рождения! Пусть в этот год наши проекты развиваются так же быстро, как ваши стратегии.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Руководитель, с Днём Рождения! Пусть этот год принесет вам столько же успеха, сколько принесли ваши мудрые решения в прошлом.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, начальник! Работать под вашим руководством легко и приятно - рост показателей говорит сам за себя.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Уважаемый босс, с Днём Рождения! Пусть в этом году наша команда будет такой же эффективной, как вы в момент принятия важных решений.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Руководитель, с праздником! Пусть ваша работоспособность будут настолько высокой, что даже кофемашина вам позавидует.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"711": [
		{
			"text": "Мой пушистый друг, с Днём Рождения! Пусть в этот год ты продолжишь удивлять нас своими веселыми прыжками и шалостями.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Рождения, мой четвероногий кумир! Пусть этот год принесёт тебе столько же вкусных угощений, сколько ты заслуживаешь.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Милый питомец, с праздником! Пусть этот год будет полон уютных мест для дрёмы и веселых игр.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Пушистик, с Днем Рождения! Пусть твои хитрости будут такими же невероятными, как твои способности вылавливать закуски.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
		{
			"text": "Любимец, с праздником! Пусть этот год принесет тебе столько же ласки и внимания, сколько ты приносишь нам каждый день.",
			"photo_id": "AgACAgIAAxkBAAIB8GXJEOyhUNMN7jk1yim9Udl6Kd43AAKg0zEbDkJISoxUR5ZjzDMtAQADAgADdwADNAQ"
		},
	],
	"60": [
		{
			"text": "Мам, с Днём Студента! Теперь я знаю еще больше, чем ты думаешь, что я знаю. Спасибо за поддержку и стратегический запас пельменей в морозильнике!",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая мамочка, с праздником! Ты всегда верила в меня, даже когда я не мог понять, что такое интегралы.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Мама, с Днём Студента! Твоя кухня – моя вторая родная земля, а вот аудитории – просто очень странные места.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Мамуля, с праздником! Ты всегда была моим живым фонтаном знаний и столько раз спасала меня от обезвоживания)",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая мама, с Днём Студента! Помни, что даже если сейчас я знаю больше, чем ты, я всегда буду твоим вечным ребенком.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"61": [
		{
			"text": "Папа, с Днём Студента! Теперь я не только могу программировать, но и разбираться в том, почему твой компьютер не работает.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой папа, с праздником! Твои бесконечные советы по ремонту теперь дополняются моими знаниями о структурах данных.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Папочка, с Днём Студента! Ты всегда был моим гуру во всем, кроме, возможно, алгебры абстрактных систем.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Папа, с праздником! Спасибо, что помог мне стать студентом, без тебя я бы не справился.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой отец, с Днём Студента! Твои истории о студенческой жизни стали еще более смешными теперь, когда я сам в этом участвую.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"62": [
		{
			"text": "Бабушка, с Днём Студента! Теперь я могу понять, почему твой рецепт борща так важен – это как алгоритм успеха в студенческой жизни!",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая бабушка, с праздником! Твои сказки про студенческие годы вдохновляют меня на новые подвиги и приключения.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Бабушка, с Днём Студента! Ты всегда говорила, что учеба – это как спорт, и теперь я знаю, как много кардио требует экзамен)",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Бабуля, с праздником! Твои советы о том, как вести себя в обществе, пригодились мне не только на семейных вечерах, но и на лекциях.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая бабушка, с Днём Студента! Твой секрет долголетия – не только в правильном питании, но и в постоянном желании учиться новому.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"63": [
		{
			"text": "Дедушка, с Днём Студента! Теперь я знаю, что важнее: ваш опыт или мои современные технологии. Спасибо за бесценные советы!",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой дедушка, с праздником! Твои рассказы о том, как вы учились, вдохновляют меня на подвиги в мире науки.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дедуля, с Днём Студента! Твои забавные истории про студенческие выходки всегда добавляют позитива в мою жизнь.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Деда, с праздником! Твои советы по учебе оказались такими же полезными, как и рассказы о том, как вы учились без интернета.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": 'Дедушка, с Днём Студента! Теперь я знаю, что ваши "баттлы" на парах были не менее захватывающими, чем современные онлайн-дискуссии.',
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"64": [
		{
			"text": 'Братик, с Днём Студента! Теперь я могу похвастаться, что у меня есть брат, который понимает, что такое "зондирование уравнений".',
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой брат, с праздником! Ты всегда был моим лучшим ресурсом для криптографических атак на пароли Wi-Fi.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Братишка, с Днём Студента! Твои розыгрыши и эксперименты в лаборатории стали неотъемлемой частью моей студенческой жизни.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": 'Братец, с праздником! Теперь, когда я студент, я ещё больше ценю наши "научные" дебаты за обедом.',
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой брат, с Днем Студента! Ты мой главный союзник в борьбе с преподавателями и теми, кто захватывает стиральные машины в нашей общаге.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"65": [
		{
			"text": "Сестричка, с Днём Студента! Я так и не понял, почему ты всегда была такой умной – это гены или секретные знания, полученные в университете?",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая сестричка, с праздником! Ты всегда была моим главным подсказчиком по домашним заданиям, а теперь и по студенческим проблемам.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Сестрёнка, с Днём Студента! Твои секреты успешной учебы теперь сослужат мне хорошую службу в мире науки и знаний.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Сестричка, с праздником! Ты не только моя родная сестра, но и мой кумир в мире студенческих открытий и экспериментов.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": 'Дорогая сестра, с Днём Студента! Теперь, когда я в университете, я еще больше ценю наши "научные" вечера с попкорном и сериалами.',
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"66": [
		{
			"text": "Любимый, с Днём Студента! Теперь, когда ты еще умнее, я в два раза сильнее тебя люблю.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой, с праздником! Ты – мой студент-герой, пора отметить твой успех чем-то особенным.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Мой ученый, с Днём Студента! Твоя умственная гибкость и творческий подход к учебе заставляют мое сердце биться быстрее.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Любимый, с праздником! Теперь ты еще ближе к своей цели, и я горжусь быть твоим научным вдохновением и поддержкой.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Мой умница, с Днём Студента! Пусть этот год принесет тебе не только знания, но и море веселья и смеха.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"67": [
		{
			"text": "Дорогая, с Днём Студента! Теперь, когда ты студентка, ты еще больше вдохновляешь меня своим интеллектом и решимостью.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Любимая, с праздником! Набирайся знаний и умений - у тебя всё получится.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Моя учёная, с Днём Студента! Твои достижения в учёбе – это еще одна причина восхищаться тобой каждый день.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогая, с праздником! Ты – источник вдохновения. Ты справишься с любым гранитом науки!",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Моя гениальная половинка, с Днём Студента! Горжусь тобой - ты умница!",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"68": [
		{
			"text": 'Родственник, с Днем Студента! Теперь ты официально член клуба "Люди, которые сдали экзамены".',
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой родственник, с праздником! Пусть этот учебный год будет таким же увлекательным, как твои предыдущие приключения в мире знаний.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Родственник, с Днём Студента! Ты всегда был гением, и теперь ты ещё ближе к своей мечте.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Дорогой, с праздником! Твоя учёба – это настоящее путешествие, и мы гордимся, что можем идти вместе.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Родной, с Днём Студента! Твои успехи кое-что доказали всем нам - не сбивайся с курса!",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"69": [
		{
			"text": "Коллега, с Днём Студента! Пусть в этот учебный год ты будешь получать отличные оценки не только на работе, но и в университете!",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Студента, коллега! Карьерный рост не заставит себя ждать - всё в твоих руках.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, уважаемый студент-коллега! Пусть в этом году твои проблемы решаются так же легко, как задачи в экзаменационных билетах.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Коллега, с Днём Студента! Пусть твои идеи на работе будут реализованы, а учёба принесёт лишь радость.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Студента, коллега! Пусть все сессии пройдут легко и быстро.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"610": [
		{
			"text": "Уважаемый руководитель, с Днём Студента! Пусть ваши проекты будут так же успешными, как вы во время защиты курсовых.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Руководитель, с Днём Студента! Пусть ваше руководство будет столь же выверенным, как ответы на экзамене.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "С праздником, уважаемый начальник-студент! Пусть в этот год вы отлично справитесь и с бизнесом, и с учёбой.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Уважаемый босс, с Днём Студента! Пусть в этом году ваша команда будет такой же согласованной, как хорошо оркестр.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Руководитель, с праздником! Пусть ваш профессионализм будет настолько высоким, что даже студенты будут вас воспринимать как пример для подражания.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"611": [
		{
			"text": "Мой мурлыкающий друг, с Днём Студента! Пусть этот год принесет тебе столько же увлекательных игр, сколько студентам на лекциях.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "С Днём Студента, моя лапочка-студентка! Пусть в учебном году ты будешь столь же исключительной, как твои успехи у дрессировщика.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Милый питомец, с праздником! Пусть этот год принесет тебе столько же веселья и ласки, сколько ты даришь мне каждый день.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Пушистик, с Днём Студента! Пусть твои приключения в новом году будут столь же захватывающими, как студенческие вечеринки.",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
		{
			"text": "Любимец, с праздником! Научишь меня так же жалобно смотреть, выпрашивая вкусняшку?",
			"photo_id": "AgACAgIAAxkBAAIB8WXJFFg7L5oNvtVYZ9-_aTrEVTQqAAKy0zEbDkJISgoRqqCghEq_AQADAgADdwADNAQ"
		},
	],
	"3": [
		{
			"text": """
5 сентября отмечается Международный день Благотворительности.  В этот день важно  поддерживать благотворительные и общественные инициативы, направленных на улучшение жизни людей по всему миру.
Поздравьте наших подопечных с этим важным событием, кликнув на кнопку.
Им будет очень приятно!
Фонд Соломон вас очень любит!""",
			"photo_id": "AgACAgIAAxkBAAIB8mXJGMEboGxDA6X5-qY2E2-m0_89AALK0zEbDkJISrlNkNKcRXuoAQADAgADdwADNAQ",
			"button_text": "Поддержать",
			"button_link": "https://www.google.com/"
		},
	],
	"4": [
		{
			"text": """
3 декабря - Щедрый вторник, является глобальной инициативой, объединяющей людей по всему миру в поддержке благотворительных организаций и добрых проектов. Мы предлагаем вам поздравить наших подопечных кликнув ниже!
Фонд Соломон вас очень любит!""",
			"photo_id": "AgACAgIAAxkBAAIB82XJGQlWKQF4GpdBR322fNDXVs-6AALM0zEbDkJISkZWXQe7DsieAQADAgADdwADNAQ",
			"button_text": "Поддержать",
			"button_link": "https://www.google.com/"
		}
	]

}


def add_persons():
	for x, itr in enumerate(persons):
		Person.create(name=itr, place=x).save()


def add_titles():
	for x, itr in enumerate(default_events):
		Title.create(name=itr, is_default=True, place=x).save()


def add_photos():
	photo = ""
	for i, itr in enumerate(greetings):
		if greetings[itr][0]["photo_id"] != photo:
			photo = greetings[itr][0]["photo_id"]
			Photo.create(photo_id=photo).save()


def add_events():
	for i, itri in enumerate(default_events):
		if i not in (3, 4):
			for x, itrx in enumerate(persons):
				for z, itrz in enumerate(greetings[f"{i}{x}"]):
					Event.create(
						title=Title.get(Title.name == itri),
						is_default=True,
						text=itrz["text"],
						photo=Photo.get(Photo.photo_id == itrz["photo_id"]),
						person=Person.get(Person.name == itrx),
					).save()
		else:
			for z, itrz in enumerate(greetings[f"{i}"]):
				Event.create(
					title=Title.get(Title.name == itri),
					is_default=True,
					text=itrz["text"],
					photo=Photo.get(Photo.photo_id == itrz["photo_id"]),
					button_text=itrz["button_text"],
					button_link=itrz["button_link"]
				).save()


if __name__ == "__main__":
	if input('Подтверди заполнение БД ("YES"):') == "YES":
		add_persons()
		add_titles()
		add_photos()
		add_events()
