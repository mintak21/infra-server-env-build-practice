# 概要
以下の練習を行うためのリポジトリ。
※ApplicationサーバはFlaskで作成。このサーバの処理内容はhealthチェックAPIくらいしか持たない(この部分はこのリポジトリのコア目的ではないため)
1. Nginx+Gunicorn(uWSGI)にてWebサーバ+APPサーバの構成をローカルで立ち上げられるようにする。
2. 1の設定をheroku上でデプロイ。
3. DBサーバ(PostgresSQL)をかませる。
4. Webサーバ、APPサーバ、DBサーバをDocker化
5. Ansibleを利用してさらなる管理効率化

# Tips
## Gunicorn
WSGI対応しているWebアプリケーション
- 起動方法
```bash
gunicorn {エントリポイントとなるファイル名}:{ファイル内のFlaskインスタンス変数名}
```
※停止はCtrl+C

- オプション
   - -c {CONFIG_FILE} : 設定ファイルの指定。ファイルの記載内容は http://docs.gunicorn.org/en/latest/settings.html


## Nginx
- 起動
```bash
nginx
```

- 起動しているかの確認
```bash
ps aux | grep nginx
# ここでnginx: master processと出てきた場合はnginxが動いている。

# PORTの確認ができるコマンド
lsof -i -P | grep nginx
# nginx     41845 mintak    6u  IPv4 0x595e7f947462ada5      0t0  TCP *:9123 (LISTEN)
```

- 停止
```bash
nginx -s stop
```
※　psで調べたPIDでkillするのでもよい。

- オプション
   - -c {CONFIG_FILE} : 設定ファイルの指定。default: (/usr/local)/etc/nginx/nginx.conf

### Configファイルの設定
- 一例
```conf
# Workerプロセスは1つ
worker_processes  1;

# events部分は必須
events {
	worker_connections 512; #コネクション数の制限
}

# http部分も必須
http {
    server {
    	listen  9123;
    	server_name INFRA-PRACTICE-NGINX;
	charset UTF-8;

	proxy_set_header    Host    $host;
	proxy_set_header    X-Real-IP    $remote_addr;
        proxy_set_header    X-Forwarded-Host       $host;
        proxy_set_header    X-Forwarded-Server    $host;
        proxy_set_header    X-Forwarded-For    $proxy_add_x_forwarded_for;

        # localhost:9123/をporxy_passにリバースプロキシでつなぐ
    	location / {
        	proxy_pass http://0.0.0.0:9876;
    	}
    }
}
```
