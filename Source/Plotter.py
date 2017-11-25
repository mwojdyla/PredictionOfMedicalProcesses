import matplotlib.pyplot as plt


class Plotter(object):

	def __init__(self):
		pass

	def plot(self, x_axis, y_axis, x_label, y_label):
		plt.plot(x_axis, y_axis)
		plt.ylabel(y_label)
		plt.xlabel(x_label)
		plt.show()
