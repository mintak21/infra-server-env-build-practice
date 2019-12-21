# Sever Socket
# host = '127.0.0.1'
# port = os.getenv('PORT', 9876)
# bind = str(host) + ':' + str(port)
# ポートの問題でソケット通信に変更
bind = 'unix:///tmp/nginx.socket'

# Debugging
reload = False

# Logging
accesslog = '-'
loglevel = 'info'

# Proc Name
proc_name = 'Infrastructure-Practice-Flask'

# Worker Processes
workers = 1
worker_class = 'sync'


def when_ready(server):
    # Nginxサーバに対して、gunicornがコネクション確立していることを通知するために必要
    # Heroku/nginx-buildpacks専用設定
    open('/tmp/app-initialized', 'w').close()
