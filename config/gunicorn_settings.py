import os

# Sever Socket
host = '0.0.0.0'  # Flaskは外部公開を許していないので、基本これ
port = os.getenv('PORT', 9876)

bind = str(host) + ':' + str(port)
# bind = 'unix:/tmp/nginx.socket'

# Debugging
reload = True

# Logging
accesslog = '-'
loglevel = 'debug'

# Proc Name
proc_name = 'Infrastructure-Practice-Flask'

# Worker Processes
workers = 1
worker_class = 'sync'
