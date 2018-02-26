class DataSample(object):

	def __init__(self, data_list):
		self.date  = data_list[0]
		self.time  = data_list[1]
		self.code  = int(data_list[2])
		self.value = float(data_list[3])

	def show(self):
		print('Date: {0} | Time: {1} | Code: {2} | Value: {3}'.format(
			self.date, self.time, self.code, self.value))