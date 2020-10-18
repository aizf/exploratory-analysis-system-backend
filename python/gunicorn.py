import os
import platform
import multiprocessing

# debug = True
# loglevel = 'deubg'
# 服务地址（adderes:port）
bind = '0.0.0.0:5000'

# if platform.system() == 'Windows':
#     # win机器路径
#     log_path = os.path.join(os.path.dirname(__file__), 'log')
# else:
#     # 服务器路径
#     log_path = '/log'

# print(log_path)
# pidfile = log_path + '/gunicorn.pid'
# logfile = log_path + '/debug.log'

# 启动的进程数（获取服务器的cpu核心数*2+1）
# workers = multiprocessing.cpu_count() * 2 +1
workers = 2
