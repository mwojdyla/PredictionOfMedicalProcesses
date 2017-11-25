from DataStructure import DataStructure


class DataManager(object):

	def __init__(self, data):
		self.data = data

	def get_converted_data(self):
		dates = self._get_single_dates()

		for date in dates:
			single_date_samples = self.filter_data_by_date(date).samples
			

	def _get_single_dates(self):
		single_dates = []

		all_dates = [sample.date for sample in data.samples]
		for date in all_dates:
			if date not in single_dates:
				single_dates.append(date)

		return single_dates

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
