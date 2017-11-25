from Utils import data_codes
from DataStructure import DataStructure, DataSample

import re
import logging

logger = logging.getLogger('root')

class FileParser(object):

	def __init__(self):
		pass

	def parse(self, files):
		patients_data = []

		for file in files:
			data_struct = DataStructure(file)

			with open(file, 'r') as data_file:
				for line in data_file.readlines():
					splitted_line = line.split()

					if self._is_ignored_line(splitted_line, file):
						continue

					data_struct.samples.append(DataSample(splitted_line))
			patients_data.append(data_struct)

		return patients_data

	def _is_ignored_line(self, line_parts, file):
		try:
			return not self._is_valid_parts_length(line_parts) or \
				   not self._is_valid_date_format(line_parts[0], file) or \
				   not self._is_valid_time_format(line_parts[1], file) or \
				   not self._is_valid_code(line_parts[2], file) or \
				   not self._is_valid_value(line_parts[3], file)
			
		except ValueError:
			logger.info('ValueError caught in {0} with {1}'.format(
				file, line_parts))
			return True

	def _is_valid_parts_length(self, parts):
		return len(parts) == 4

	def _is_valid_date_format(self, date, file):
		date_pattern = re.compile('\d{2}-\d{2}-\d{4}')
		if date_pattern.match(date) == None:
			logger.warning('{0}: {1} didn\'t match to date pattern'.format(
				file, date))
			return False

		return True

	def _is_valid_time_format(self, time, file):
		time_pattern = re.compile('\d{1,2}:\d{1,2}')
		if time_pattern.match(time) == None:
			logger.warning('{0}: {1} didn\'t match to time pattern'.format(
				file, time))
			return False

		return True

	def _is_valid_code(self, code, file):
		if int(code) not in data_codes:
			logger.warning('{0}: {1} is unknown data code'.format(file, code))
			return False

		return True

	def _is_valid_value(self, value, file):
		if float(value) < 0:
			logger.warning('{0}: Negative value occured'.format(file))
			return False

		return True
