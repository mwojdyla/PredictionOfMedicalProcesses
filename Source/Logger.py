import logging


class Logger(object):

	@classmethod
	def setup_custom_logger(cls, name):
		formatter = logging.Formatter(
			fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

		# handler = logging.StreamHandler()
		# handler.setFormatter(formatter)
		handler = logging.FileHandler('Logs/logs.log', mode='w')
		handler.setFormatter(formatter)

		logger = logging.getLogger(name)
		logger.setLevel(logging.DEBUG)
		logger.addHandler(handler)
		return logger
