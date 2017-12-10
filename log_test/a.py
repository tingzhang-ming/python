# -*- coding: utf-8 -*-
import os
import logging
import sys

# logging.basicConfig(format='log-%(levelname)s: %(message)s',
#                     stream=sys.stdout,
#                     level=logging.getLevelName(
#                         os.environ.get('LOG_LEVEL', 'INFO')))
log = logging.getLogger()


# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("AppName")

# 指定logger输出格式
formatter = logging.Formatter('logger-%(asctime)s %(levelname)-8s: %(message)s')

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值

# 为logger添加的日志处理器
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.DEBUG)

# 输出不同级别的log
logger.debug('this is debug info')
logger.info('this is information')
logger.warn('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critical message')
log.debug('this is debug info')
log.info('this is information')
log.warn('this is warning message')
log.error('this is error message')
log.fatal('this is fatal message, it is same as logger.critical')
log.critical('this is critical message')

# 2016-10-08 21:59:19,493 INFO    : this is information
# 2016-10-08 21:59:19,493 WARNING : this is warning message
# 2016-10-08 21:59:19,493 ERROR   : this is error message
# 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
# 2016-10-08 21:59:19,493 CRITICAL: this is critical message
