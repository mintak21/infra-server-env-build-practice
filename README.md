# 概要
以下の練習を行うためのリポジトリ。
※ApplicationサーバはFlaskで作成。このサーバの処理内容はhealthチェックAPIくらいしか持たない(この部分はこのリポジトリのコア目的ではないため)
1. Nginx+Gunicorn(uWSGI)にてWebサーバ+APPサーバの構成をローカルで立ち上げられるようにする。
2. 1の設定をheroku上でデプロイ。
3. DBサーバ(PostgresSQL)をかませる。
4. Webサーバ、APPサーバ、DBサーバをDocker化
5. Ansibleを利用してさらなる管理効率化
