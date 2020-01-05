# debianベースのpythonイメージをベースとする
FROM python:3.8-slim-buster

# 設定ファイルの転送(適当な場所が思いつかないので/app直下)
RUN mkdir -p /app/config
COPY requirements.txt /app/requirements.txt
COPY config/gunicorn_settings.py /app/config/gunicorn_settings.py
COPY flask_app.py /app/flask_app.py

# パッケージのインストール
RUN pip install -r /app/requirements.txt

EXPOSE 9876
# cdにあたるコマンド
WORKDIR /app

# run実行時のコマンド
# ENTRYPOINT->CMDでCMDはrunのときの引数で上書きすることが可能
ENTRYPOINT [ "gunicorn", "flask_app:app" ]
CMD [ "-c", "/app/config/gunicorn_settings.py" ]
