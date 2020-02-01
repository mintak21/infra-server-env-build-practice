# debianベースのpythonイメージをベースとする
FROM python:3.8-alpine

# 設定ファイルの転送(適当な場所が思いつかないので/app直下)
RUN mkdir -p /app/config
COPY . /app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# パッケージのインストール
RUN pip install -r /app/requirements.txt

EXPOSE 9876
# cdにあたるコマンド
WORKDIR /app

# run実行時のコマンド
# ENTRYPOINT->CMDでCMDはrunのときの引数で上書きすることが可能
ENTRYPOINT [ "gunicorn", "flask_app:app" ]
CMD [ "-c", "config/gunicorn_settings.py" ]
