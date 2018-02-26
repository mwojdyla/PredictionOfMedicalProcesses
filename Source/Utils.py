from os import listdir
from os.path import dirname, abspath

import logging
import math


data_codes = [33, 34, 35, 48, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]

logger = logging.getLogger('root')

class Utils(object):
	
	@classmethod
	def get_diabetes_data_files(cls):
		directory = Utils.get_diabetes_data_directory()

		return [directory + file for file in listdir(directory) if 'data' in file]

	@classmethod
	def get_diabetes_data_directory(cls):
		dir_name = 'Diabetes-Data'
		main_dir = dirname(dirname(abspath(__file__)))
		diabetes_data_dir = \
			[dir_ for dir_ in listdir(main_dir) if dir_ == dir_name][0]
		
		return abspath(diabetes_data_dir) + '/'

	@classmethod
	def compute_euclidean_distance(cls, vector_x, vector_w):
		distance = 0.0

		if len(vector_x) != len(vector_w):
			logger.warning('Sizes of vectors are different!')
			return distance

		for index in range(len(vector_x)):
			distance = distance + (vector_x[index] - vector_w[index]) ** 2

		return math.sqrt(distance)

	@classmethod
	def calculate_difference(cls, vector_x, vector_w):
		difference = []

		if len(vector_x) != len(vector_w):
			logger.warning('Sizes of vectors are different!')
			return difference

		for index in range(len(vector_x)):
			difference.append(vector_x[index] - vector_w[index])

		return difference

	@classmethod
	def multiply_vector(cls, scalar, vector):
		multiplication_result = []

		for component in vector:
			multiplication_result.append(scalar * component)

		return multiplication_result

	@classmethod
	def calculate_sum(cls, vector_x, vector_w):
		sum_ = []

		if len(vector_x) != len(vector_w):
			logger.warning('Sizes of vectors are different!')
			return sum_

		for index in range(len(vector_x)):
			sum_.append(vector_x[index] + vector_w[index])

		return sum_

	@classmethod
	def calculate_influence(cls, winner, neuron, radius):
		distance = Utils.compute_euclidean_distance(winner.weights, neuron.weights)
		counter = -(distance ** 2)
		denominator = 2 * (radius ** 2)

		return math.exp(counter / denominator)
