import os

# Sever Socket
host = '127.0.0.1'
port = os.getenv('PORT', 9876)

bind = str(host) + ':' + str(port)

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
