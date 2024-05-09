DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
.ENV = --env-file .env
APP_FILE = dockerfiles/app.yaml
APP_CONTAINER = arbitrum-app


.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

