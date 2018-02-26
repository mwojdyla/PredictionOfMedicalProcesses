from DataSample import DataSample


class DataManager(object):

	def __init__(self, data):
		self.data = data

	def get_converted_data(self):
		dates = self._get_unique_dates()

		converted_data = []
		for date in dates:
			filtered_samples = self.filter_data_by_date(date)
			averaged_time_samples = self.average_time(filtered_samples)
			converted_data = converted_data + averaged_time_samples

		return converted_data

	def _get_unique_dates(self):
		unique_dates = []

		for date in [sample.date for sample in self.data]:
			if date not in unique_dates:
				unique_dates.append(date)

		return unique_dates

	def _get_unique_times(self, samples):
		unique_times = []

		for sample in samples:
			if sample.time not in unique_times:
				unique_times.append(sample.time)

		return unique_times

	def average_time(self, samples):
		times = self._get_unique_times(samples)

		averaged_data = []
		for unique_time in times:
			same_times = [elem for elem in samples if elem.time == unique_time]
			sample_copy = same_times[0]
			sample_copy.value = sum([elem.value for elem in same_times]) / len(same_times)
			averaged_data.append(sample_copy)

		# return averaged_time_samples
		# times = set(map(lambda x: x.time, samples))
		# same_samples = [[sample for sample in samples if sample.time == t] for t in times]
		# averaged_data = [(sum(group) / len(group)) for group in same_samples]

		return averaged_data


	def filter_data_by_date(self, date):
		return [sample for sample in self.data if sample.date == date]

	def filter_data_by_code(self, code):
		return [sample for sample in self.data if sample.code == code]
