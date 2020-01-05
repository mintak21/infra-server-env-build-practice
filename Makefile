APP_SERVER_TAG = debian:app-server
WEB_SERVER_TAG = centos:web-server

build: build_app build_web

build_app:
	docker build -f deployment/dockerfiles/app-server/Dockerfile -t $(APP_SERVER_TAG) .

build_web:
	docker image build -f deployment/dockerfiles/web-server/Dockerfile -t $(WEB_SERVER_TAG) .

run_app: build_app
	docker run --rm --name app-server --network bridge $(APP_SERVER_TAG)

run_web: build_web
	docker run --rm --name web-server -p 9090:9123 --network bridge $(WEB_SERVER_TAG)

stop:
	docker stop $(APP_SERVER_TAG)
	docker stop $(WEB_SERVER_TAG)

restart:
	docker restart $(APP_SERVER_TAG)
	docker restart $(WEB_SERVER_TAG)

cleanup:
	docker image rm $(APP_SERVER_TAG)
	docker image rm $(WEB_SERVER_TAG)

# ファイルを作成しないことを事前にmakeへ通知
.PHONY: run_app run_web cleanup stop restart
