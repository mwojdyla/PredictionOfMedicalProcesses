#Python packages

#Source files
from DataSample import *
from Logger import Logger
from FileParser import FileParser
from DataManager import DataManager
from KohonenNetwork import KohonenNetwork
from Utils import Utils
from Plotter import Plotter


logger = Logger.setup_custom_logger('root')
logger.info('START!')

files = Utils.get_diabetes_data_files()
files.sort()

data_parser = FileParser()
patients_data = data_parser.parse(files)
manager = DataManager(patients_data[1])
averaged_data = manager.get_converted_data()



network = KohonenNetwork([[123,221,333,421], [35,50,70,20], [402,412,321,100]] , 3, 3, 100)
network.process_self_organization()
print("######################################################")
network.show_weights()

# plotter = Plotter()
# plotter.plot(['04-23-1991', 'Tuesday', 'Wednesday'], [2, 4, 6], 'Time', 'Value')