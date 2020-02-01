COMPOSE_DIR=_deployment/docker-compose

build:
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yaml build

build-no-cache:
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yaml build --no-cache

run: build
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yaml up

stop:
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yaml stop

restart:
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yaml restart

cleanup: stop
	docker-compose -f ${COMPOSE_DIR}/docker-compose.yaml down --rmi all -v

# ファイルを作成しないことを事前にmakeへ通知
.PHONY: build build-no-cache run stop restart cleanup
