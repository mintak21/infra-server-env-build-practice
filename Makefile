COMPOSE_DIR=_deployment/docker-compose

build:
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yml build

rebuild:
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yml build --no-cache

run: build
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yml up

start:
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yml start

cleanup:
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yml down --rmi all -v

# ファイルを作成しないことを事前にmakeへ通知
.PHONY: run build rebuild start cleanup
