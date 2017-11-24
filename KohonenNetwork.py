from Utils import Utils

import random
import math


class KohonenNetwork(object):

	def __init__(self, input_layer, rows, columns, iterations):
		if type(input_layer) != list:
			raise TypeError('Input layer is not a type of list')

		for index in range(len(input_layer)):
			if type(input_layer[index]) != list:
				raise TypeError(
					'{0}. input is type of {1} instead of list'.format(
						index, type(input_layer[index])))

		self.initial_learning_rate = 0.1
		self.iterations_number = iterations
		self.map_radius = max(rows, columns) // 2
		self.time_constant = self.iterations_number / math.log(self.map_radius)
		self.neurons_number = rows * columns
		self.input_layer = input_layer
		self.computional_layer = None 

	def process_self_organization(self):
		self._process_initialization()

		for iteration in range(self.iterations_number):
			for input_unit in self.input_layer:
				winner, index = self._process_competition(input_unit)
				radius, neighbourhood = self._process_cooperation(winner, 
					iteration)
				self._process_adaptation(input_unit, winner, neighbourhood,
					radius, iteration)
				self.computional_layer.insert(index, winner)

	def _process_initialization(self):
		dimension = len(self.input_layer[0])

		self.computional_layer = self._create_map_of_neurons(
			self.neurons_number, dimension)

	def _create_map_of_neurons(self, neurons_number, dimension):
		neurons = []
		for i in range(neurons_number):
			new_neuron = Neuron(dimension)
			neurons.append(new_neuron)

		return neurons

	def _process_competition(self, input_unit):
		neuron_index = None
		closest_distance = 1000000.0

		for index in range(len(self.computional_layer)):
			distance = Utils.compute_euclidean_distance(
				input_unit, self.computional_layer[index].weights)

			if distance < closest_distance:
				neuron_index = index
				closest_distance = distance

		return self.computional_layer.pop(neuron_index), neuron_index

	def _process_cooperation(self, winner, iteration):
		neighbours = []

		neighbourhood_radius = \
			self.map_radius * math.exp(-iteration / self.time_constant)
		for neuron in self.computional_layer:
			distance = Utils.compute_euclidean_distance(
				winner.weights, neuron.weights)

			if distance <= neighbourhood_radius:
				neighbours.append(neuron)

		return neighbourhood_radius, neighbours

	def _process_adaptation(self, input_unit, winner, neighbourhood,
		radius, iteration):
		learning_rate = \
			self.initial_learning_rate * math.exp(-iteration / self.time_constant)

		for neuron in neighbourhood:
			influence = Utils.calculate_influence(winner, neuron, radius)
			vectors_difference = Utils.calculate_difference(
				input_unit, neuron.weights)
			product = Utils.multiply_vector(
				influence * learning_rate, vectors_difference)
			neuron.weights = Utils.calculate_sum(neuron.weights, product)


	
class Neuron(object):

	def __init__(self, dimension):
		self.weights = self._initialize_weights(dimension)

	def _initialize_weights(self, dimension):
		random.seed()

		connection_weights = []
		for i in range(dimension):
			component = random.random()
			connection_weights.append(component)

		return connection_weights
