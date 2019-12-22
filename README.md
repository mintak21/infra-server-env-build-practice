# 概要
以下の練習を行うためのリポジトリ。
※ApplicationサーバはFlaskで作成。このサーバの処理内容はhealthチェックAPIくらいしか持たない(この部分はこのリポジトリのコア目的ではないため)
1. Nginx+Gunicorn(uWSGI)にてWebサーバ+APPサーバの構成をローカルで立ち上げられるようにする。
2. 1の設定をheroku上でデプロイ。
3. DBサーバ(PostgresSQL)をかませる。
4. Webサーバ、APPサーバ、DBサーバをDocker化
5. AnsibleやK8sを利用してさらなる管理効率化

# Tips
- Step1まとめ　https://qiita.com/mintak21/items/eeba4654a0db21abcb1c


- まずNginx-Gunicorn間はソケットで。(ポートがややこしいような気がしたのと、この例ばかり出てきたため)
- heroku buildpack追加
```bash
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-nginx
heroku buildpacks:add heroic/python
```
作業ブランチをHerokuのmasterへデプロイする方法
```bash
git push heroku 2_heroku_deploy:master --force
git push {ブランチ名}:master --force
```
heroku上に入り込んでbashの操作を行う
```bash
heroic run bash
```

## Ref
https://medium.com/@eserdk/heroku-nginx-gunicorn-flask-f10e81aca90d
