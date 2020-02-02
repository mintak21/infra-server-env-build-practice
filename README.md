# 概要
以下の練習を行うためのリポジトリ。
※ApplicationサーバはFlaskで作成。このサーバの処理内容はhealthチェックAPIくらいしか持たない(この部分はこのリポジトリのコア目的ではないため)
1. Nginx+Gunicorn(uWSGI)にてWebサーバ+APPサーバの構成をローカルで立ち上げられるようにする。[Completed]
2. 1の設定をheroku上でデプロイ。[Skip]
3. Webサーバ、APPサーバをDocker化。[Completed]
4. 3をdocker-composeで管理[Completed]
5. DBサーバ(PostgresSQL)をかませる。[Here]
6. Ansible等を利用してさらなる管理効率化。

# Commands

* make run     - appサーバ、webサーバ、DBサーバのコンテナをdocker-composeにて起動。基本はこれを利用。
* make rebuild - appサーバ、webサーバイメージを再構築
* make cleanup - app-server、web-server、db-serverのコンテナ、イメージを破棄、およびボリュームを削除

# Access

http://localhost:8000/
http://localhost:8000/health/
http://localhost:8000/test/

# Tips

- psycopg2のインストール

Pythonのpostgres向けDriverではもっとも使われているよう。
単純に`pip install`でインストールしようとしてもうまく行かなかった。

  - python:alpineイメージ側：`gcc python3-dev musl-dev postgresql-dev` が予め必要。2.8系のバージョンならこれでうまくいく。2.7系はこれでもwheelに失敗する(未解決)
  - ローカル`MacOS`では`export LDFLAGS="-L/usr/local/opt/openssl/lib" export CPPFLAGS="-I/usr/local/opt/openssl/include"`を指定したところインストールできた。

```Dockerfile:Dockerfile
RUN apk update \
  && apk add --virtual .build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
```

- Flaskにおける秘密情報の設定方法
Flaskで推奨されている方法は、`instance`フォルダを作成、その配下に`key-value`形式のファイルを配置して、
`config.from_pyfile`関数により、呼び出すというもの。(もちろん`.gitignore`に追加して管理対象外とする)
アプリインスタンスを作成する際に、`instance_relative_config`を`True`としておくと、**実行時にインスタンスを作成したパス**直下の`instance`ディレクトリが対象となる。
なので、このディレクトリ構成の場合、`flask_app.pyのあるディレクトリ/instance` となる。
今回は、Docker側で環境設定を設定、これによる切替を行い、`instance`での読み込みは行わない。



# ref

- [flaskの設定方法まとめ](https://www.subarunari.com/entry/2018/03/17/%E3%81%84%E3%81%BE%E3%81%95%E3%82%89%E3%81%AA%E3%81%8C%E3%82%89_Flask_%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E3%81%BE%E3%81%A8%E3%82%81%E3%82%8B_%E3%80%9CConfiguration%E3%80%9C)
- [flask-storingdata](http://exploreflask.com/en/latest/storing.html#sqlalchemy)
- [flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [SQLAlchemy:postgres](https://docs.sqlalchemy.org/en/13/dialects/postgresql.html?highlight=postgres#module-sqlalchemy.dialects.postgresql.psycopg2)
- [psycopg](https://www.psycopg.org/docs/install.html)
- [alpineイメージでpsycopgインストールが失敗する](https://github.com/psycopg/psycopg2/issues/684)
- [ローカルMacOSにpsycopgがインストールできない](https://github.com/psycopg/psycopg2/issues/997)
