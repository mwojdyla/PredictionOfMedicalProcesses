#Python packages

#Source files
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

plotter = Plotter()
plotter.plot(['04-23-1991', 'Tuesday', 'Wednesday'], [2, 4, 6], 'Time', 'Value')
network = KohonenNetwork([[1,2,3], [3,2,1], [1,4,1], [5,1,3]], 6, 5, 20)
network.process_self_organization()