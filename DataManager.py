from DataStructure import DataStructure


class DataManager(object):

	def __init__(self, data):
		self.data = data

	def filter_data_by_date(self, date):
		filtred_data = DataStructure()
		filtred_data.samples = \
			[sample for sample in data.samples if sample.date == date]

		return filtred_data

	def filter_data_by_code(self, code):
		filtered_data = DataStructure()
		filtered_data.samples = \
			[sample for sample in data.samples if sample.code == code]

		return filtered_data
