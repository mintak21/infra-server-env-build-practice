# debianベースのpythonイメージをベースとする
FROM python:3.8-alpine

# 設定ファイルの転送(適当な場所が思いつかないので/app直下)
RUN mkdir -p /application/config
COPY . /application
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# パッケージのインストール
RUN apk update \
  && apk add --virtual .build-deps gcc musl-dev \
  && apk add postgresql-dev \
  && pip install -r /application/requirements.txt \
  && apk --purge del .build-deps


EXPOSE 9876
# cdにあたるコマンド
WORKDIR /application

# run実行時のコマンド
CMD [ "gunicorn", "flask_app:app", "-c", "config/gunicorn_settings.py" ]
