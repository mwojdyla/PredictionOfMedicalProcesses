class DataStructure(object):

	def __init__(self, path=None):
		self.samples = []
		self.file_path = path


class DataSample(object):

	def __init__(self, data_list):
		self.date  = data_list[0]
		self.time  = data_list[1]
		self.code  = int(data_list[2])
		self.value = float(data_list[3])