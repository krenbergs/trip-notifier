include .env.development
export $(shell sed 's/=.*//' .env.development)

mkdb:
	docker run --name $${DOCKER_CONTAINER_NAME} -p $${POSTGRES_PORT}:$${POSTGRES_PORT} -e POSTGRES_PASSWORD=$${POSTGRES_PASSWORD} -e POSTGRES_DB=$${POSTGRES_DB} -e POSTGRES_USER=$${POSTGRES_USER} -d postgres
	@until docker exec $${DOCKER_CONTAINER_NAME} pg_isready -U $${POSTGRES_USER}; do \
		sleep 1; \
	done
	PYTHONPATH=. python src/utils/setup_database.py

rmdb:
	docker remove --force $${DOCKER_CONTAINER_NAME}

resetdb:
	PYTHONPATH=. python scripts/reset_database.py

showdb:
	PYTHONPATH=. python src/utils/show_database.py

popdb:
	PYTHONPATH=. python src/utils/populate_database.py

runapp:
	poetry run uvicorn src.app:app --reload