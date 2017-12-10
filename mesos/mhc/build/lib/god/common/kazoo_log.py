import logging
from logging import handlers

class Logger(logging.Logger):
	def __init__(self):
		super(Logger, self).__init__(self)

	def set_log_dir(self, infofile):
		infoh = logging.handlers.RotatingFileHandler(infofile, maxBytes = 50*1024*1024, backupCount = 10)
		infoh.setLevel(logging.INFO)

 		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s')
		infoh.setFormatter(formatter)

		self.addHandler(infoh)