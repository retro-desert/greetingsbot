# Стандартные праздники
from data.config import BIRTHDAY, THANKSGIVING, LOVE_DAY, MARCH_8, SEPTEMBER_1, DECEMBER_3, NEW_YEAR, \
	JANUARY_25, MOTHER, FATHER, GRANDMOTHER, GRANDFATHER, FRIEND, GIRLFRIEND, LOVER_MAN, LOVER_WOMAN, BROTHER, SISTER, \
	RELATIVE, COLLEAGUE, MANAGER, PET, TEACHER, STUDENT, SCHOOLBOY, NEW_MEMBER
from models import Event, Person, Title, Photo

default_events = (
	BIRTHDAY,
	THANKSGIVING,
	LOVE_DAY,
	MARCH_8,
	SEPTEMBER_1,
	DECEMBER_3,
	NEW_YEAR,
	JANUARY_25,
	NEW_MEMBER,
)

greetings = {
	LOVE_DAY: {
		MOTHER: [
			{
				"text": "Мама, ты – моя настоящая любовь! Спасибо за бесконечное терпение и нежность. С Днём Святого Валентина!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Мамочка, поздравляю тебя с Днём Святого Валентина! Твои ласковые слова и забота делают каждый мой день особенным.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая мама, с Днём Святого Валентина! Наши сердца бьются в унисон - люблю тебя!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя, моя самая родная мамочка, с Днём Святого Валентина! Скучаю по тебе сильно, обнимаю тебя крепко, люблю тебя нежно!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Милая мама, с Днём Святого Валентина! Пусть огонь нашей любви горит ещё ярче!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		FATHER: [
			{
				"text": "Пап, сердечно поздравляю тебя в этот любвеобильный день! Твои советы и поддержка – для меня бесценны.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С любовью и благословением в День Святого Валентина для самого заботливого и мудрого папы. Ты – настоящий герой!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Папочка, поздравляю тебя с Днём Святого Валентина! Твоя помощь и забота делают каждый день удачным и ярким.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Папа, привет! День Святого Валентина пришёл) Твоя сила и мудрость – моё вдохновение.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой папа, с Днём Святого Валентина! Твоя любовь – как крепкий фундамент, на котором строится моя жизнь.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},

		],
		GRANDMOTHER: [
			{
				"text": "Дорогая бабушка, с Днём Святого Валентина! Твоя любовь – как самый мягкий и теплый плед в холодные дни.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Бабушка, с любовью и благословением в этот особенный день! Твои советы и забота  – для меня самое ценное сокровище.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая бабушка, с Днём Святого Валентина! Твоя любовь – как светлячок, озаряющий мой путь.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Бабушка, в этот день любви и тепла, хочу сказать тебе, как я тебя люблю! С Днём Святого Валентина!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина, любимая бабушка! Ты – мой образец доброты и мудрости, я тобой горжусь.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		GRANDFATHER: [
			{
				"text": "Дорогой дедушка, с Днём Святого Валентина! Твоя любовь – как тёплое солнце, согревающее моё сердце.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дедушка, с любовью и уважением в этот особенный день! Твоя мудрость и стойкость – для меня вечный источник вдохновения.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя, мой самый заботливый дедушка, с Днём Святого Валентина! Твои советы – мой надёжный компас в жизни.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дедушка, в этот день хочу сказать тебе, как я тебя ценю и люблю! С Днём Святого Валентина!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина, дедушка! Ты – мой герой и учитель, я тобой горжусь.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		FRIEND: [
			{
				"text": "С Днём Святого Валентина! Пусть любовь наполнит сердце радостью!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с Днём Святого Валентина! Желаю любить, мечтать и радоваться!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина тебя! Счастья, любви и терпения!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Спешу поздравить тебя с Днём Святого Валентина! Желаю взаимной любви и стопроцентного счастья!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "На календаре День Святого Валентина! Поздравляю тебя и желаю всего самого приятного и радостного!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		GIRLFRIEND: [
			{
				"text": "Поздравляю тебя с Днём Святого Валентина! Пусть сердце бьётся чаще от настоящей любви!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина тебя! Желаю головокружительной любви и умопомрачительного счастья!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Ура! 14 февраля! Поздравляю с Днём Святого Валентина! Счастья, удачи и любви!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с Днём Святого Валентина, желаю любить, мечтать и улыбаться!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина! Пусть в душе царит умиротворение, а в сердце - любовь!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		LOVER_MAN: [
			{
				"text": "Поздравляю тебя с Днём Святого Валентина! Желаю взаимной любви и гармонии.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю с Днём Святого Валентина! Счастья, улыбок и любви!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Прими мои поздравления с Днём Святого Валентина! Пусть любовь будет долгой и счастливой!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина! Желаю радоваться, улыбаться и любить!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "День Святого Валентина пришёл! Пусть всё будет легко и приятно!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		LOVER_WOMAN: [
			{
				"text": "Поздравляю тебя с Днём Святого Валентина! Желаю побольше солнечных дней и счастливых моментов.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю с Днём Святого Валентина! Счастья, любви и радости тебе и твоим близким!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина тебя! Пусть в жизни случается только хорошее!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Прими мои поздравления с Днём Святого Валентина! Любовь превыше всего - пусть мечты сбываются!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с Днём Святого Валентина! Весна уже близко - любви и терпения.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		BROTHER: [
			{
				"text": "Братишка, с Днём Святого Валентина! Твоя поддержка и дружба – для меня как спасательный круг в океане жизни.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Брат, с любовью и благословением в этот особенный день! Твоя сила и решимость всегда меня вдохновляют.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой брат, с Днём Святого Валентина! Твоя весёлая натура и доброе сердце делают каждый день особенным.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Брат, с Днём Святого Валентина! Твоя заразительная улыбка – мой источник радости и оптимизма.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С тобой всегда весело, брат! С Днём Святого Валентина! Твоя жизнерадостность – мое бесценное богатство.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		SISTER: [
			{
				"text": "Сестрёнка, с Днём Святого Валентина! Твоя забота и нежность – как лучики солнца в моей жизни.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая сестричка, с любовью и благословением в этот особенный день! Твоя умная голова и доброе сердце – радость моих дней.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Сердечно поздравляю самую лучшую сестру с Днём Святого Валентина! Твоя поддержка – мой надёжный причал.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Сестричка, с Днём Святого Валентина! Твоя улыбка и веселый настрой делают каждый момент весёлым и особенным.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая сестра, с Днём Святого Валентина! Твоя открытость и чувство юмора радуют моё сердце!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		RELATIVE: [
			{
				"text": "С Днём Святого Валентина, родной(ая)! Твоя мудрость – мой самый надежный компас.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина, родной(ая)! Твоя улыбка – это солнце, согревающее наши сердца.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Родственник(ца) мой(моя), с любовью и благословением в этот особенный день! Твоя поддержка – мое убежище.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина, дорогой(ая) родственник(ца)! Твоя дружба – высшая ценность.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Родной(ая), с любовью и теплом в этот особенный день! Твоя забота – как летний дождь, питающий корни нашей семейной любви.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		COLLEAGUE: [
			{
				"text": "Уважаемый(ая) коллега, с Днём Святого Валентина! Твой профессионализм и отзывчивость – пример для подражания.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина, уважаемый(ая) коллега! Твоя трудовая активность и ответственность вдохновляют нашу команду.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Коллега, с любовью к профессии и благодарностью за твою отличную работу! С Днём Святого Валентина!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Уважаемый(ая) коллега, с Днём Святого Валентина! Твоя инициатива и умение решать нестандартные задачи впечатляют.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Святого Валентина, уважаемый(ая) коллега! Твои идеи и креативный подход делают наши проекты уникальными.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		MANAGER: [
			{
				"text": "С благодарностью и уважением поздравляю вас, руководитель(ница), с Днём Святого Валентина! Ваши организаторские способности окрыляют и зовут на трудовые подвиги.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Руководитель(ница), с любовью к работе и уважением к сотрудникам! С Днём Святого Валентина! Ваша лидерские качества вдохновляют на новые достижения.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Уважаемый(ая) руководитель(ница), с Днем Святого Валентина! Ваше внимание к деталям и стремление к совершенству – наша гордость.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Руководитель(ница), с Днём Святого Валентина! Ваша способность мотивировать – наше секретное оружие.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С благодарностью за ваши трудовые усилия, руководитель(ница)! С Днём Святого Валентина! Ваша справедливость и мудрость –  наша верная опора.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		PET: [
			{
				"text": "Мой дорогой пушистик (или кличка питомца), с Днём Святого Валентина! Твои ласки и верность – моя истинная радость.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С любовью и теплом поздравляю моего верного друга с Днём Святого Валентина! Твои ласковые мурчания делают мою жизнь яркой.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя, мой пушистик (или кличка питомца), с Днём Святого Валентина! Твоя преданность – моё главное сокровище.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Мой милый друг, с Днём Святого Валентина! Твои нежные прикосновения дарят мне настоящий уют.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником, мой хвостатый друг! Твои весёлые выходки – моё непередаваемое счастье.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
	},
	MARCH_8: {
		MOTHER: [
			{
				"text": "Мам, с 8 марта! Твоя суперсила – как у настоящей супергероини! Ты мегамама!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая мама, с Международным женским днём тебя! Пусть твои выходные будут такими же волшебными, как ты!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": 'Мамочка, с 8 марта! Ты – наш главный "шеф-повар" и чемпион по наведению порядка!',
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником, мама! Ты – наша любимая командирша в битве за семейное благополучие!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Мамуля, с 8 марта! Ты – настоящая звезда нашего семейного шоу!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
		],
		GRANDMOTHER: [
			{
				"text": "Бабушка, с 8 марта! Твои советы –  золото - их ценность только растёт!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая бабушка, с Международным женским днём тебя! Твои кулинарные шедевры – достойны самой высокой оценки!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Бабуля, с восьмым марта! Твоя мудрость – как луч света в наших семейных тоннелях)",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": 'С праздником, бабушка! Ты – наша главная "колдунья", превращаешь обыденные моменты в волшебные.',
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Любимая бабушка, с 8 марта! Твой стиль и элегантность вне времени!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
		],
		GIRLFRIEND: [
			{
				"text": "Ура! 8 марта! Пусть вместе с тюльпанами в дом придёт весна и радость!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с 8 марта! Желаю удачи, любви и хорошей погоды!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "С Международным женским днём тебя! Солнца, цветов и улыбок тебе и твоим близким!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "С 8 марта тебя! Пусть сбудутся мечты и исполнятся все заветные желания!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "А вот и мои поздравления с 8 марта подъехали! Желаю тебе всех благ, успехов на работе и крепкого здоровья!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
		],
		LOVER_WOMAN: [
			{
				"text": "С 8 марта тебя! Желаю побольше цветов, радости и счастливых моментов!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с праздником! Пусть эта весна сделает сказку былью!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С 8 марта! Пусть солнечные лучи поскорее отогреют твоё сердечко!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Международным женским днём тебя! Желаю жить играючи и получать удовольствие от каждого дня!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником! Весна идёт - весне дорогу! Всего наилучшего тебе!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		SISTER: [
			{
				"text": "Сестричка, с 8 марта! Твои советы – как мультитул в нашем семейном ящике с инструментами.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая сестра, с Международным женским днём тебя! Твои кулинарные эксперименты – наше любимое гастрономическое приключение!",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Сестрёнка, с 8 марта! Твоя энергия – как магнит, притягивающий позитив и радость.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя, сестрица, с 8 марта! Твоя сила – в твоей уникальности.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Сестра, с праздником! Твоя доброта – как волшебная палочка, делающая наш мир ярче.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
		],
		COLLEAGUE: [
			{
				"text": "Коллега, с 8 марта! Твой профессионализм – как бриллиант в короне нашей команды.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "С Международным женским днём тебя, коллега! Твои идеи – как вишенка на торте нашего проекта.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Коллега, с 8 марта! Ты настоящий командный игрок – в положительном результате всегда есть твоя заслуга.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником, дорогая коллега! Твоя энергия вдохновляет всех нас.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Коллега, с 8 марта! Твоя добродушная улыбка – как витаминка для тонуса в офисе.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
		],
		MANAGER: [
			{
				"text": "Уважаемый руководитель, с 8 марта! Для нас вы маяк, указывающий путь к успеху.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "С Международным женским днём, уважаемый начальник! Ваше руководство – гарантия нашего общего успеха.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Руководитель, с 8 марта! Ваше лидерство – как факел, освещающий наш трудовой путь.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником, уважаемый руководитель! Ваша поддержка помогает достигать целей.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Руководитель, с 8 марта! Ваш профессионализм – как надёжный  двигатель, что обеспечивает поступательный рост к новым вершинам.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
		],
		PET: [
			{
				"text": "Мой милый пушистик (или кличка), с 8 марта! Твои мурчания – лучшая музыка для моих ушей.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником, моя пушистая радость! Твои весёлые игры отвлекают от забот и не дают скучать.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Питомец, с 8 марта! Твоя преданность – настоящая драгоценность моей жизни.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "С Международным женским днём, мой четвероногий друг! Твоя ласка – как исцеляющий бальзам для моей души.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
			{
				"text": "Мой любимчик, с праздником! Твои шалости – как радуга в серых буднях моей жизни.",
				"photo_id": "AgACAgIAAxkBAAIMRGXorko639OF49EoriAzqV2LWr8kAAI71jEbZiVIS1Oc0LKtG92kAQADAgADdwADNAQ"
			},
		],
	},
	SEPTEMBER_1: {
		TEACHER: [
			{
				"text": 'Примите поздравления с началом учебного года! Успехов и терпения всем, кто уже учит и ещё только учится.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "С 1 сентября! Пусть этот учебный год будет плодотворным и интересным.",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Поздравляю с Днём Знаний! Желаю искать и находить, учить и учиться!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Всего наилучшего в новом учебном году! Ваша любознательность - пример для подражания.",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Ура! Снова 1 сентября! Спасибо, что делитесь своими знаниями и умениями!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		STUDENT: [
			{
				"text": 'Поздравляю с 1 сентября! Знание - сила, пора стать ещё немного сильнее!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "С 1 сентября! Пусть гранит науки будет сладок. Удачи на экзаменах!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Поздравляю с Днём Знаний! Желаю успехов и терпения - курсовая сама себя не напишет.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "С началом учебного года тебя! Учиться никогда не поздно, но начать лучше прямо сейчас.",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Новый учебный год начинается - мои поздравления! Иногда будет сложно, но всегда будет интересно!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		SCHOOLBOY: [
			{
				"text": 'С 1 сентября тебя! Пора учиться, учиться и учиться, но каникулы не за горами - всё будет хорошо!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Знаний! Пусть в школе будет интересно и весело!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Поздравляю тебя с началом учебного года! Знай, что я всегда готов помочь.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "1 сентября на календаре - пора в школу! Впитывай знания как губка, но и отдыхать не забывай!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Опять внезапно начался сентябрь - учителя уже ждут, не опаздывай хотя бы сегодня!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		MOTHER: [
			{
				"text": 'Мам, с 1 сентября! Надеюсь, в этом "учебном году" ты не опоздаешь на наши встречи и обеды!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая мама, с Днем Возвращения в Режим! Поднимай настроение, как будто поднимаешь пульс на физкультуре.",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Мамочка, с праздником! Пусть этот "школьный год" принесет тебе отличные оценки в категории "Домашний миротворец".',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Мама, календарь перевернули и снова 1 сентября. Ты сильная, ты справишься - поздравляю с началом нашего общего учебного года!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Мамуля, с 1 сентября тебя! Пусть День знаний принесёт тебе только приятные эмоции!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		FATHER: [
			{
				"text": 'Папа, с 1 сентября! Надеюсь, ты готов к "урокам" по выживанию в семье!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Дорогой папочка, с Днем Возвращения в "Школу Жизни"! Пусть наше семейное коворкинг-пространство будет весьма успешным.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Папуля, с праздником! Пусть каждый домашний эксперимент принесет тебе заслуженную награду.",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Пап, тебя в школу вызывают - с цветами! 1 сентября на дворе - да будет праздник! ",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Папа, наступил День знаний! Поздравляю тебя и торжественно обещаю - учиться, учиться и ещё раз учиться)",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		GRANDMOTHER: [
			{
				"text": 'Бабушка, с 1 сентября! В этом "учебном году" ждем от тебя уроки "Секреты Волшебной Кулинарии"!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Дорогая бабушка, с Днем Возвращения к "Учебнику Жизни"! Твои истории – лучший урок для понимания семейных традиций.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Бабушка, с праздником! Пусть этот "школьный год" принесет тебе только смех и радость.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Бабуля, сегодня красный день календаря - День знаний! Ты всегда говорила, что знания - сила, пусть новый учебный год придаст сил всем нам.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Бабушка, с 1 сентября тебя! Новый учебный год это хорошо забытый старый) Будем делать домашние задания вместе?',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		GRANDFATHER: [
			{
				"text": 'Дедушка, с 1 сентября! Готов ли ты к "урокам по возвращению в детство" с внуками?',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Дорогой дедушка, с Днем Возвращения к "Школе Веселья"! Твои уроки юмора – наш фирменный стиль.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Дедуля, с праздником! Пусть этот "школьный год" принесет тебе невероятные приключения с нашими весёлыми внуками.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Дедушка, на дворе опять 1 сентября - начинается новый учебный сезон. Без твоего опыта и знаний нам не обойтись!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Дедушка, на нас опять наступает 1 сентября. Спасибо, что словом и делом помогаешь в нелёгком деле обучения.",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		FRIEND: [
			{
				"text": 'Поздравляю тебя с началом учебного года! Удачи, успехов и терпения!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'С 1 сентября тебя! Пусть грандиозные планы воплотятся в жизнь!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Поздравляю тебя с Днём знаний! Желаю богатырского здоровья и безмятежного счастья!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "1 сентября! Прими мои поздравления! Пусть новые достижения не заставят себя ждать.",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с 1 сентября! Желаю тебе отличного настроения и пусть всё получится!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		GIRLFRIEND: [
			{
				"text": 'С 1 сентября тебя! Желаю тебе найти что-то новое и интересное!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Поздравляю тебя с Днём знаний! Пусть благополучие станет твоим извечным спутником!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Поздравляю тебя с 1 сентября! Счастья, здоровья, удачи и чистого неба над головой!',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с началом учебного года! Желаю тебе всего самого наилучшего, самого интересного и полезного!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Спешу поздравить тебя с 1 сентября! Пусть всё будет так, как ты захочешь!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		LOVER_MAN: [
			{
				"text": "Поздравляю тебя с 1 сентября! Учиться никогда не поздно - успехов!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём знаний! Пусть любознательность не даёт скучать!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с Днём знаний! Желаю учиться только на чужих ошибках!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С 1 сентября тебя! Пусть эта осень будет тёплой и солнечной!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Вот и лето прошло - 1 сентября. Поздравляю тебя с началом учебного года и желаю научиться чему-нибудь новенькому!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		LOVER_WOMAN: [
			{
				"text": "С 1 сентября тебя! Пусть золотая осень станет вторым летом!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю с началом учебного года! Желаю побольше удачи, тепла и улыбок!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с 1 сентября! Пусть в доме царит гармония и любовь!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю с Днём знаний! Желаю радоваться жизни и узнавать новое!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Знание - сила! Да пребудет с тобой сила! С 1 сентября тебя!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		BROTHER: [
			{
				"text": 'Братишка, с 1 сентября! Готов ли ты к "школьным заметкам" о том, как ты занимаешь ванную вечером?',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Брат, с Днем Возвращения к "Школе Братства"! Ты – мой личный гуру по семейным приключениям.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Братик, с праздником! Пусть этот "школьный год" принесёт нам новые рекорды по придумыванию весёлых прозвищ.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Брат мой, крепись - впереди новый учебный год. Мы будем вместе в нашей борьбе за знания!",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Брат, 1 сентября надвигается! Ты ведь поможешь мне с домашкой, правда?",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
		SISTER: [
			{
				"text": 'Сестричка, с 1 сентября! Готова ли ты к "урокам женской магии" в этом семейном учебном году?',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Дорогая сестра, с Днем Возвращения к "Школе Женственности"! Твои лайфхаки – неотъемлемая часть нашего семейного арсенала.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": 'Сестренка, с праздником! Пусть этот "школьный год" принесет нам невероятные сюрпризы и весёлые моменты.',
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Сестрица, привет! У нас опять 1 сентября - давай праздновать, уроки только завтра)",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
			{
				"text": "Сестра, этот день настал. Школы опять открыли свои двери и ждут учеников. Мы выдержим это и будем гордиться собой.",
				"photo_id": "AgACAgIAAxkBAAIMRWXormwWGQzb6CeAnZH9ZmE61ObRAAJY1jEbZiVIS5SXUgk9Cho5AQADAgADdwADNAQ"
			},
		],
	},
	NEW_YEAR: {
		MOTHER: [
			{
				"text": "Мам, с наступающим Новым Годом! Пусть твои рецепты семейного счастья  будут такими же волшебными, как твои кулинарные шедевры!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогая мамочка, с Новым Годом! Твоя любовь делает нас счастливыми!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Мама, с праздником! Просто будь собой и не переживай по пустякам - у нас всё получится!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С наступающим, мама! Береги себя, будь умничкой - мы вместе, значит всё будет хорошо!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Мамуля, с Новым Годом! Пусть наши семейные посиделки случаются чаще. Для счастья не нужен повод.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		FATHER: [
			{
				"text": "Пап, с наступающим Новым Годом! Пусть твои забавные истории не кончаются, а бюджет выдержит «подарочную» нагрузку!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогой папочка, с Новым Годом! С нетерпением ждём твоих новых кулинарных экспериментом!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Папа, с праздником! Пусть наступающий год принесет тебе не только хорошую погоду для барбекю, но и больше времени для семейного шопинга.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": 'С наступающим, папа! Пусть новый год станет для тебя поводом открыть новую страницу в своем "блоге отца" с еще более креативными советами.',
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Папуля, с Новым Годом! Пусть наши семейные поединки в компьютерных играх будут такими же захватывающими, как и твои звёздные стратегии на работе!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		GRANDMOTHER: [
			{
				"text": "Бабушка, с наступающим Новым Годом! Твоё вязание в 100 раз выше любой высокой моды.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогая бабушка, с Новым Годом! Будь счастлива, не болей и почаще радуй своей стряпнёй!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Бабуля, с праздником! Пусть новый год принесет тебе побольше солнечных дней на даче!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": 'С наступающим, бабушка! Ты замечательно читаешь внукам сказки перед сном, а как насчёт собственной  книги "Мемуары Гиперактивной Бабушки"?',
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Любимая бабушка, с Новым Годом! Пусть наши встречи будут такими же теплыми, как твои пледы, и такими же  вдохновляющими, как твои рассказы о своих приключениях!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		GRANDFATHER: [
			{
				"text": "Дедушка, с наступающим Новым Годом! Пусть в новом году ты продолжишь удивлять своими историями, с годами они становятся только интереснее.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогой дедушка, с Новым Годом! Твой опыт и оптимизм заряжает нас положительной энергией.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Дедуля, с праздником! Желаю побольше тёплых дней и увлекательных путешествий на дачу и не только)",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С наступающим, дедушка! В новом году ты научишь нас играть в шахматы, а мы поможем освоить смартфон - идёт?",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Любимый дедушка, с Новым Годом! План такой: болеть меньше, двигаться больше и ежедневно радоваться жизни. Приступаем немедленно!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		FRIEND: [
			{
				"text": 'С Новым годом! Пусть всё будет хорошо и предсказуемо. Удачи во всех начинаниях!',
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Поздравляю тебя с Новым годом! Желаю сохранить оптимизм и стать лучшей версией себя!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "И снова с Новым годом! Любви, дружбы, хорошей погоды и добрых вестей!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С Новым годом! С новым счастьем! Пусть небо будет безоблачным, а встречи - желанными!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Поздравляю с Новым годом! Желаю добра и здоровья! Пусть хлопоты будут только приятными.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		GIRLFRIEND: [
			{
				"text": "С Новым годом! Удачи в делах, успехов в работе и побольше солнечных дней в наступающем году!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Поздравляю тебя с Новым годом! Желаю любви, тепла и исполнения всех желаний!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С наступающим! Пусть Новый год принесёт только приятные эмоции!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С Новым годом! Впереди только радость! Всего наилучшего тебе!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Поздравляю с Новым годом! Желаю здоровья и благополучия! Счастье не за горами.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		LOVER_MAN: [
			{
				"text": "С наступающим Новым Годом! Желаю тебе найти новые поводы для радости!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником! Пусть новый год превзойдёт все самые смелые ожидания.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Новым Годом! С новым счастьем! Успехов в делах, удачи во всём и крепчайшего здоровья тебе!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С наступающим! Пусть новый год принесёт мешок долгожданных подарков!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с Новым Годом! Пусть твои самые амбициозные планы воплотятся в жизнь!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		LOVER_WOMAN: [
			{
				"text": "С Новым Годом! Желаю бороться и искать, найти и не сдаваться!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Новым Годом тебя! Пусть в новом году не будет места для скуки. Успехов, улыбок и удачи!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником! Да будет так: мечты исполнятся, трудности закончатся и всем станет хорошо!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с Новым Годом! Пусть каждый день будет полон радости, улыбок и приятных сюрпризов!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Новым Годом тебя! Уверен, что всё наладится - впереди ещё много интересного!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		BROTHER: [
			{
				"text": "Братишка, с наступающим Новым Годом! Пусть этот год принесет тебе не только новые рекорды в видеоиграх, но и успехи на работе.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Брат, с Новым Годом! Желаю новых рекордов в фитнес-клубе, на стадионе и на спортплощадке!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": 'С праздником, бро! Надеюсь, что  этот год принесет тебе не только признание на работе, но и победу в семейных "спортивных дуэлях".',
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С наступающим, брат! Пусть в новом году будет больше креатива и творчества.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": 'Братишка, с Новым Годом! Пусть наши "бои" за пульт от телевизора будут такими же зрелищными, как чемпионаты по футболу!',
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		SISTER: [
			{
				"text": "Сестричка, с наступающим Новым Годом! Желаю твоим мечтам сбываться! Будь здорова и счастлива, как никогда прежде!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогая сестра, с Новым Годом! Увлекайся и увлекай, радуйся и радуй, удивляйся и удивляй! Люблю тебя!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Сестренка, с праздником! Пусть этот год принесёт тебе не только успехи в работе, но и безудержное веселье в кругу семьи.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С наступающим, сестричка! Пусть новый год станет для тебя поводом открыть новые горизонты в путешествиях и увлекательных занятиях.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогая сестра, с Новым Годом! Пусть наши семейные вечера будут такими же теплыми, как и твои объятия, и такими же весёлыми, как твои шутки!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		RELATIVE: [
			{
				"text": "Родной/родная, с Новым Годом! Пусть этот год будет таким же удивительным, как разговоры, которые мы ведём в кругу семьи.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С Новым Годом, родственник! Пусть в этом году наши семейные собрания будут такими же шумными и весёлыми, как салют в полночь.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С праздником, родня! Пусть каждый момент с вами будет таким же согревающим, как чашка горячего чая в морозный вечер.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогие родственники, с Новым Годом! Удачи, любви и терпения всем нам.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Родные мои, с Новым Годом! Желаю оставаться собой, помогать друг другу и чаще встречаться вне сети.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		COLLEAGUE: [
			{
				"text": "Коллега, с Новым Годом! Пусть в нашем офисе будет столько же вкусного, сколько в праздничном салате!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С Новым Годом, коллеги! Желаю щёлкать рабочие задачи как орешки. Орешки с варёной сгущёнкой, конечно)",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С праздником, уважаемые коллеги! Любая цель будет нам по плечу, если коллектив сплотится. И для начала плотненько закусим)",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Коллеги, с Новым Годом! Пусть наша команда будет такой же согласованной, как огоньки на гирлянде.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Уважаемые сотрудники, с Новым Годом! Пусть в этом году в нашем офисе будет столько же хороших идей, сколько игрушек на ёлке.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		MANAGER: [
			{
				"text": "Уважаемый руководитель, с Новым Годом! Пусть в этом году наши проекты будут такими же успешными, как ваша стратегия управления.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С Новым Годом, уважаемый начальник! Пусть в нашем подразделении будет столько же вдохновения, сколько в ваших мотивационных речах.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С праздником, руководитель! Впереди Новый год и новые свершения, команда готова и ждёт ваших указаний.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С Новым Годом, босс! Пусть наши корпоративные цели будут достигнуты так же быстро, как летит пробка из бутылки.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Руководитель, с Новым Годом! Ваша мудрость в паре с нашей исполнительностью сделают реальностью самые смелые мечты!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
		PET: [
			{
				"text": "Мой пушистик (или кличка), с Новым Годом! Пусть этот год будет полон новых игрушек, вкусняшек и прогулок.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "С Новым Годом, мой четвероногий друг! Ты образец позитивного настроения и увлечённости!",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Милый питомец, с праздником! Пусть новогодние угощения будут вкусными, как твои любимые лакомства.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Пушистик, с Новым Годом! Пусть каждый день будет наполнен игрой, уютом и лаской.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
			{
				"text": "Любимец, с Новым Годом! Ты настоящий друг и неповторимый комочек счастья, не болей и не грусти, когда меня нет рядом.",
				"photo_id": "AgACAgIAAxkBAAIMRmXorpWzC7oSPY7sc_Gxvl1zzIYFAAJa1jEbZiVIS0S2zAABCgnEZAEAAwIAA3cAAzQE"
			},
		],
	},
	BIRTHDAY: {
		MOTHER: [
			{
				"text": "Мам, с Днём Рождения! Ты всегда молодая и стильная, даже когда пытаешься понять, как пользоваться смайликами в сообщениях!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогая мамочка, с праздником! Пусть этот год будет таким же увлекательным, как твои попытки разобраться в мире социальных сетей.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С Днём Рождения, мама! Обязательно помогу тебе выучить все современные мемы!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Мамуля, с праздником! Наслаждайся жизнью, радуй нас своим вниманием и не унывай - всё будет хорошо!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Мам, с Днём Рождения! Дуй на свечи, загадывай желания, радуйся каждому дню - впереди ещё много интересного!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		FATHER: [
			{
				"text": "Пап, с Днём Рождения! Поздравляю тебя с тем, что ты такой же молодой, как и твои анекдоты, которые мы слышим каждый год)",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогой папочка, с праздником! Пусть этот день будет столь же запоминающимся, как твои шутки в семейных чатах.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С Днём Рождения, папа! Поздравляю тебя с тем, что ты всегда такой весёлый, даже когда пытаешься настроить технику.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Папуля, с праздником! Пусть этот год будет полон смеха, как и твои попытки научиться использовать новые приложения на телефоне.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Пап, с Днём Рождения! Оставайся собой, празднуй весело, будь самым нарядным - это твой день!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		GRANDMOTHER: [
			{
				"text": "Бабушка, с Днём Рождения! Поздравляю тебя с тем, что ты такая же мудрая, как и твои советы, которые мы любим слушать каждый раз.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогая бабушка, с праздником! Пусть этот год будет таким же теплым, как твои объятия, когда мы приходим в гости.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С Днём Рождения, бабушка! Поздравляю тебя с тем, что ты ничего не забываешь, особенно истории из детства.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": 'Бабуля, с праздником! Пусть твой день будет столь же сладким, как твои превосходные пироги.',
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Бабушка, с Днём Рождения! Мы любим тебя, ценим и очень скучаем! Ты почётный хранитель нашей семейной мудрости.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		GRANDFATHER: [
			{
				"text": "Дедушка, с Днём Рождения! Поздравляю тебя с тем, что ты такой же обстоятельный, как твои рассказы о прежних временах.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогой дедушка, с праздником! Пусть этот год будет таким же весёлым, как  твои анекдоты.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С Днём Рождения, дедуля! Поздравляю тебя с тем, что ты всегда такой добрый, как и твои советы о жизни.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дедушка, с праздником! Пусть этот день будет столь же активным, как твои прогулки по парку каждый утро.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогой дед, с Днём Рождения! Поздравляю тебя с тем, что ты всё такой же крепкий, как твои объятия.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		FRIEND: [
			{
				"text": "С днём рождения тебя! Ты пример для подражания - удачи в делах!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Поздравляю с днём рождения! Пусть праздник будет весёлым, угощение - вкусным, а подарок - желанным!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Поздравляю тебя с днём рождения! Желаю крепкого здоровья, верных друзей и славных дел!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С днём рождения! Пир на весь мир или скромное застолье - непростой выбор. Удачи!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "А вот и день рождения подкрался… Поздравляю! Желаю тебе всего самого лучшего!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		GIRLFRIEND: [
			{
				"text": "С днём рождения тебя! Если меняться, то только к лучшему!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Поздравляю тебя с днём рождения! Желаю быть счастливой и не беспокоиться по пустякам.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С днём рождения! Пусть что-то чудесное произойдёт как можно быстрее!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "О! День рождения! Поздравляю-поздравляю! Верь в себя и всё получится!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Пора поздравить тебя с днём рождения! Желаю быть счастливой! Быть, а не казаться.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		LOVER_MAN: [
			{
				"text": "С Днём Рождения! Пусть твои мечты сбываются! Здорово, что ты есть.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю с днём рождения! Желаю здоровья, счастья и побольше весёлых деньков!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём рождения тебя! Удачи, любви и терпения!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с днём рождения! Пусть всё будет хорошо или отлично!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю с Днём Рождения! Ты сможешь реализовать все свои планы на 100%!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		LOVER_WOMAN: [
			{
				"text": "С Днём Рождения! Всё самое интересное впереди - это точно!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с днём рождения! Самое время радоваться жизни!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Рождения! Тот самый момент настал - пора творить историю!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником! С днём рождения! Желаю любить, улыбаться и быть на седьмом небе от счастья!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Рождения! Пусть этот праздник запомнится и принесёт только позитив!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		BROTHER: [
			{
				"text": "Братан, с Днём Рождения! Поздравляю тебя с тем, что ты такой же крутой, как твои попытки выучить новый трюк на скейтборде.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогой брат, с праздником! Пусть этот год будет таким же интересным, как и твои истории о приключениях.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С Днём Рождения, братишка! Поздравляю тебя с тем, что ты всегда такой же невероятно смешной, как твои шутки и розыгрыши.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": 'Братуля, с праздником! Пусть твой день будет столь же удачным, как твои попытки сделать "селфи" на каждой вечеринке.',
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Братиша, с Днем Рождения! Поздравляю тебя с тем, что ты такой же нужный, как твои советы в сложных ситуациях.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		SISTER: [
			{
				"text": "Сестричка, с Днём Рождения! Поздравляю тебя с тем, что ты такая же красивая, как твои фотографии в соцсетях.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогая сестрёнка, с праздником! Пусть этот год будет таким же волшебным, как твои идеи для оформления комнаты.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С Днём Рождения, сестричка! Поздравляю тебя с тем, что ты всегда такая же дружелюбная, как твои сообщения с утра.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Сестрёнка, с праздником! Пусть твой день будет столь же весёлым, как твои попытки научить меня танцевать.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Сестрёнка, с Днем Рождения! Люблю тебя сильно-сильно! Ты замечательная!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		RELATIVE: [
			{
				"text": "Дорогой родственник, с Днём Рождения! Поздравляю тебя с тем, что ты такой же весёлый, как наши семейные встречи.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С Днем Рождения, родной/родная! Пусть этот год будет наполнен только приятными и интересными событиями.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С днём варенья, родственник! Надо чаще встречаться, чтобы было что вспомнить)",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Родной/родная, с Днём Рождения! Пусть этот день будет столь же тёплым, как наши семейные ужины.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогой родственник, с днём рождения! Поздравляю тебя сердечно - пусть всё будет так как ты захочешь!",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		COLLEAGUE: [
			{
				"text": "С Днем Рождения, коллега! Надеюсь, твои рабочие проекты будут такими же успешными, как попытки скрыться от шефа в курилке)",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Коллега, с Днем Рождения! Пусть в этот год у нас будет столько же смешных моментов в офисе, сколько неудачных попыток перекусить в зоне видимости веб-камеры.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С праздником, коллега! Пусть в этот год твоя продуктивность будет такой же высокой, как уровень кофеина в наших чашках.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Коллега, с Днём Рождения! Пусть этот год принесет тебе не только профессиональный успех, но и новые рекорды по количеству мемов в нашем чате.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Дорогой коллега, с праздником! Пусть твои рабочие идеи будут такими же яркими, как твои выкрутасы на корпоративах)",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		MANAGER: [
			{
				"text": "Уважаемый руководитель, с Днём Рождения! Пусть в этот год наши проекты развиваются так же быстро, как ваши стратегии.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Руководитель, с Днём Рождения! Пусть этот год принесет вам столько же успеха, сколько принесли ваши мудрые решения в прошлом.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С праздником, начальник! Работать под вашим руководством легко и приятно - рост показателей говорит сам за себя.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Уважаемый босс, с Днём Рождения! Пусть в этом году наша команда будет такой же эффективной, как вы в момент принятия важных решений.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Руководитель, с праздником! Пусть ваша работоспособность будут настолько высокой, что даже кофемашина вам позавидует.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
		PET: [
			{
				"text": "Мой пушистый друг, с Днём Рождения! Пусть в этот год ты продолжишь удивлять нас своими веселыми прыжками и шалостями.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "С Днём Рождения, мой четвероногий кумир! Пусть этот год принесёт тебе столько же вкусных угощений, сколько ты заслуживаешь.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Милый питомец, с праздником! Пусть этот год будет полон уютных мест для дрёмы и веселых игр.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Пушистик, с Днем Рождения! Пусть твои хитрости будут такими же невероятными, как твои способности вылавливать закуски.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
			{
				"text": "Любимец, с праздником! Пусть этот год принесет тебе столько же ласки и внимания, сколько ты приносишь нам каждый день.",
				"photo_id": "AgACAgIAAxkBAAIMR2XorragXM21EBuPAAEnKKNGjTJdTgACW9YxG2YlSEsJZxR8wwmdGQEAAwIAA3cAAzQE"
			},
		],
	},
	JANUARY_25: {
		MOTHER: [
			{
				"text": "Мам, с Днём Студента! Теперь я знаю еще больше, чем ты думаешь, что я знаю. Спасибо за поддержку и стратегический запас пельменей в морозильнике!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая мамочка, с праздником! Ты всегда верила в меня, даже когда я не мог понять, что такое интегралы.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Мама, с Днём Студента! Твоя кухня – моя вторая родная земля, а вот аудитории – просто очень странные места.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Мамуля, с праздником! Ты всегда была моим живым фонтаном знаний и столько раз спасала меня от обезвоживания)",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая мама, с Днём Студента! Помни, что даже если сейчас я знаю больше, чем ты, я всегда буду твоим вечным ребенком.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		FATHER: [
			{
				"text": "Папа, с Днём Студента! Теперь я не только могу программировать, но и разбираться в том, почему твой компьютер не работает.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой папа, с праздником! Твои бесконечные советы по ремонту теперь дополняются моими знаниями о структурах данных.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Папочка, с Днём Студента! Ты всегда был моим гуру во всем, кроме, возможно, алгебры абстрактных систем.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Папа, с праздником! Спасибо, что помог мне стать студентом, без тебя я бы не справился.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой отец, с Днём Студента! Твои истории о студенческой жизни стали еще более смешными теперь, когда я сам в этом участвую.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		GRANDMOTHER: [
			{
				"text": "Бабушка, с Днём Студента! Теперь я могу понять, почему твой рецепт борща так важен – это как алгоритм успеха в студенческой жизни!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая бабушка, с праздником! Твои сказки про студенческие годы вдохновляют меня на новые подвиги и приключения.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Бабушка, с Днём Студента! Ты всегда говорила, что учеба – это как спорт, и теперь я знаю, как много кардио требует экзамен)",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Бабуля, с праздником! Твои советы о том, как вести себя в обществе, пригодились мне не только на семейных вечерах, но и на лекциях.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая бабушка, с Днём Студента! Твой секрет долголетия – не только в правильном питании, но и в постоянном желании учиться новому.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		GRANDFATHER: [
			{
				"text": "Дедушка, с Днём Студента! Теперь я знаю, что важнее: ваш опыт или мои современные технологии. Спасибо за бесценные советы!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой дедушка, с праздником! Твои рассказы о том, как вы учились, вдохновляют меня на подвиги в мире науки.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дедуля, с Днём Студента! Твои забавные истории про студенческие выходки всегда добавляют позитива в мою жизнь.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Деда, с праздником! Твои советы по учебе оказались такими же полезными, как и рассказы о том, как вы учились без интернета.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": 'Дедушка, с Днём Студента! Теперь я знаю, что ваши "баттлы" на парах были не менее захватывающими, чем современные онлайн-дискуссии.',
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		FRIEND: [
			{
				"text": "Поздравляю тебя с Днём Студента! Пусть будет легко, но интересно.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Студента! Учиться, чтобы уметь - успехов тебе!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю с Днём Студента! Желаю терпения и сил - всё будет!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Спешу поздравить тебя с долгожданным Днём Студента! Пусть будет весело, разнообразно и эпично!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём вечного студента! Учись, студент! Но и развлекаться не забывай.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		GIRLFRIEND: [
			{
				"text": "Поздравляю с Днём Студента! Удачи на сессии - ты справишься!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Студента! Желаю найти своё призвание и стать экспертом в любимом деле.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Поздравляю тебя с Днём Студента! Твои старания будут вознаграждены - дерзай!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Студента тебя! Вызов брошен, гранит науки ждёт тебя - пора начинать!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Пора поздравить тебя с Днём Студента! Упорства тебе не занимать - следуй за мечтой!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		LOVER_MAN: [
			{
				"text": "Любимый, с Днём Студента! Теперь, когда ты еще умнее, я в два раза сильнее тебя люблю.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой, с праздником! Ты – мой студент-герой, пора отметить твой успех чем-то особенным.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Мой ученый, с Днём Студента! Твоя умственная гибкость и творческий подход к учебе заставляют мое сердце биться быстрее.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Любимый, с праздником! Теперь ты еще ближе к своей цели, и я горжусь быть твоим научным вдохновением и поддержкой.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Мой умница, с Днём Студента! Пусть этот год принесет тебе не только знания, но и море веселья и смеха.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		LOVER_WOMAN: [
			{
				"text": "Дорогая, с Днём Студента! Теперь, когда ты студентка, ты еще больше вдохновляешь меня своим интеллектом и решимостью.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Любимая, с праздником! Набирайся знаний и умений - у тебя всё получится.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Моя учёная, с Днём Студента! Твои достижения в учёбе – это еще одна причина восхищаться тобой каждый день.",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая, с праздником! Ты – источник вдохновения. Ты справишься с любым гранитом науки!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
			{
				"text": "Моя гениальная половинка, с Днём Студента! Горжусь тобой - ты умница!",
				"photo_id": "AgACAgIAAxkBAAIMQ2XorgpqORPEkQjZd_UzAcR95TG7AAI_1zEbndBJS676C6JGtp8nAQADAgADdwADNAQ"
			},
		],
		BROTHER: [
			{
				"text": 'Братик, с Днём Студента! Теперь я могу похвастаться, что у меня есть брат, который понимает, что такое "зондирование уравнений".',
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой брат, с праздником! Ты всегда был моим лучшим ресурсом для криптографических атак на пароли Wi-Fi.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Братишка, с Днём Студента! Твои розыгрыши и эксперименты в лаборатории стали неотъемлемой частью моей студенческой жизни.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": 'Братец, с праздником! Теперь, когда я студент, я ещё больше ценю наши "научные" дебаты за обедом.',
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой брат, с Днем Студента! Ты мой главный союзник в борьбе с преподавателями и теми, кто захватывает стиральные машины в нашей общаге.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		SISTER: [
			{
				"text": "Сестричка, с Днём Студента! Я так и не понял, почему ты всегда была такой умной – это гены или секретные знания, полученные в университете?",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогая сестричка, с праздником! Ты всегда была моим главным подсказчиком по домашним заданиям, а теперь и по студенческим проблемам.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Сестрёнка, с Днём Студента! Твои секреты успешной учебы теперь сослужат мне хорошую службу в мире науки и знаний.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Сестричка, с праздником! Ты не только моя родная сестра, но и мой кумир в мире студенческих открытий и экспериментов.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": 'Дорогая сестра, с Днём Студента! Теперь, когда я в университете, я еще больше ценю наши "научные" вечера с попкорном и сериалами.',
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		RELATIVE: [
			{
				"text": 'Родственник, с Днем Студента! Теперь ты официально член клуба "Люди, которые сдали экзамены".',
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой родственник, с праздником! Пусть этот учебный год будет таким же увлекательным, как твои предыдущие приключения в мире знаний.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Родственник, с Днём Студента! Ты всегда был гением, и теперь ты ещё ближе к своей мечте.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Дорогой, с праздником! Твоя учёба – это настоящее путешествие, и мы гордимся, что можем идти вместе.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Родной, с Днём Студента! Твои успехи кое-что доказали всем нам - не сбивайся с курса!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		COLLEAGUE: [
			{
				"text": "Коллега, с Днём Студента! Пусть в этот учебный год ты будешь получать отличные оценки не только на работе, но и в университете!",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Студента, коллега! Карьерный рост не заставит себя ждать - всё в твоих руках.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником, уважаемый студент-коллега! Пусть в этом году твои проблемы решаются так же легко, как задачи в экзаменационных билетах.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Коллега, с Днём Студента! Пусть твои идеи на работе будут реализованы, а учёба принесёт лишь радость.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Студента, коллега! Пусть все сессии пройдут легко и быстро.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		MANAGER: [
			{
				"text": "Уважаемый руководитель, с Днём Студента! Пусть ваши проекты будут так же успешными, как вы во время защиты курсовых.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Руководитель, с Днём Студента! Пусть ваше руководство будет столь же выверенным, как ответы на экзамене.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "С праздником, уважаемый начальник-студент! Пусть в этот год вы отлично справитесь и с бизнесом, и с учёбой.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Уважаемый босс, с Днём Студента! Пусть в этом году ваша команда будет такой же согласованной, как хорошо оркестр.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Руководитель, с праздником! Пусть ваш профессионализм будет настолько высоким, что даже студенты будут вас воспринимать как пример для подражания.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
		PET: [
			{
				"text": "Мой мурлыкающий друг, с Днём Студента! Пусть этот год принесет тебе столько же увлекательных игр, сколько студентам на лекциях.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "С Днём Студента, моя лапочка-студентка! Пусть в учебном году ты будешь столь же исключительной, как твои успехи у дрессировщика.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Милый питомец, с праздником! Пусть этот год принесет тебе столько же веселья и ласки, сколько ты даришь мне каждый день.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Пушистик, с Днём Студента! Пусть твои приключения в новом году будут столь же захватывающими, как студенческие вечеринки.",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
			{
				"text": "Любимец, с праздником! Научишь меня так же жалобно смотреть, выпрашивая вкусняшку?",
				"photo_id": "AgACAgIAAxkBAAIMSGXortZ0Kq3R1kDoGGtBWIjz5aplAAJc1jEbZiVIS8rbYOlTMg4kAQADAgADdwADNAQ"
			},
		],
	},
	NEW_MEMBER: {
		MOTHER: [
			{
				"text": "Мамочка, поздравляю с пополнением в семье! Новая маленькая жизнь - это счастье! Люблю тебя!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
			{
				"text": "Мама, ура - у нас пополнение! Семья стала больше - мы радуемся как дети!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
			{
				"text": "Мамуля, поздравляю тебя с рождением малыша! Пусть все будут здоровы и любимы!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
		],
		FATHER: [
			{
				"text": "Папа, поздравляю тебя с пополнением в семействе! Будем радоваться, пировать и веселиться!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
			{
				"text": "Папочка, с пополнением! На свет появилось маленькое чудо - мы ликуем, улыбаемся и машем!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
			{
				"text": "Пап, а у нас пополнение! Спасибо, что всегда нас поддерживал - ты лучший!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
		],
		GRANDMOTHER: [
			{
				"text": "Бабушка, поздравляю тебя с пополнением в семье! Появился новый повод печь пироги и торты!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
			{
				"text": "Бабуля, у нас суперновость - в семействе пополнение! Кажется, кто-то скоро опять будет нянчиться.",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
			{
				"text": "Любимая бабушка! У нас пополнение! Ты была права - это непередаваемые эмоции!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
		],
		GRANDFATHER: [
			{
				"text": "Дедушка, поздравляю тебя с пополнением в семействе! Скоро маленький человек тихонько скажет тебе: «Деда, я тебя люблю!»",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
			{
				"text": "Дедуля, пляши - у нас пополнение! Самое интересное - впереди. Здорово, что можно разделить эту радость с тобой!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
			{
				"text": "Любимый дедушка, поздравляем тебя с пополнением в семье! Будем гулять вместе - на детских площадках нас ждут великие дела!",
				"photo_id": "AgACAgIAAxkBAAIUpWZplDK0Lx7dMdUaYj5ey5JKSJrMAAJR2zEbTUtQSyXoqTav5upWAQADAgADdwADNQQ"
			},
		],
	}
}

greetings_special = {
	THANKSGIVING: {
			"text": """
5 сентября отмечается Международный день Благотворительности.  В этот день важно  поддерживать благотворительные и общественные инициативы, направленных на улучшение жизни людей по всему миру.\n
Поздравьте наших подопечных с этим важным событием, кликнув на кнопку.\n
Им будет очень приятно!\n
Фонд Соломон вас очень любит!""",
			"photo_id": "AgACAgIAAxkBAAIMSWXorxK02qdcCSY9lOmBifCv3wiWAAJg1jEbZiVIS8vMJ4k0c1NDAQADAgADdwADNAQ",
			"button_text": "Поддержать",
			"button_link": "https://clck.ru/394XDH"
	},
	DECEMBER_3: {
			"text": """
3 декабря - Щедрый вторник, является глобальной инициативой, объединяющей людей по всему миру в поддержке благотворительных организаций и добрых проектов.\nМы предлагаем вам поздравить наших подопечных кликнув ниже!\n
Фонд Соломон вас очень любит!""",
			"photo_id": "AgACAgIAAxkBAAIMSmXoryoz9eVGlhJxJZsuQYEsuYzwAAJi1jEbZiVIS2UvYpN6H763AQADAgADdwADNAQ",
			"button_text": "Поддержать",
			"button_link": "https://clck.ru/394XDH/"
	}
}


def add_titles():
	for x, itr in enumerate(default_events):
		Title.create(name=itr, is_default=True, place=x).save()


def add_events():
	for i in default_events:
		title = Title.get(Title.name == i)
		if i not in (THANKSGIVING, DECEMBER_3):
			for xi, x in enumerate(greetings[i]):
				person = Person.get_or_create(name=x, place=xi, title=title)
				for z in greetings[i][x]:
					photo = Photo.get_or_create(photo_id=z["photo_id"])
					Event.create(
						title=title,
						is_default=True,
						text=z["text"],
						photo=photo if not isinstance(photo, tuple) else photo[0],
						person=person if not isinstance(person, tuple) else person[0],
					).save()
		else:
			photo = Photo.get_or_create(photo_id=greetings_special[i]["photo_id"])
			Event.create(
				title=title,
				is_default=True,
				text=greetings_special[i]["text"],
				photo=photo if not isinstance(photo, tuple) else photo[0],
				button_text=greetings_special[i]["button_text"],
				button_link=greetings_special[i]["button_link"]
			).save()


if __name__ == "__main__":
	if input('Подтверди заполнение БД ("YES"):') == "YES":
		add_titles()
		add_events()
