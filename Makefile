build:
		docker-compose -f compose.yml build -d
up:
		docker-compose -f compose.yml up -d
down:
		docker-compose -f compose.yml down