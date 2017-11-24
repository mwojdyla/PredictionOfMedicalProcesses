#Python packages
from os import listdir

#Source files
from Logger import Logger
from FileParser import FileParser
from DataManager import DataManager
from KohonenNetwork import KohonenNetwork
from Utils import directory


logger = Logger.setup_custom_logger('root')
logger.info('START!')

files = [directory + file for file in listdir(directory) if 'data' in file]
files.sort()

data_parser = FileParser()
patients_data = data_parser.parse(files)

manager = DataManager(patients_data[0])

network = KohonenNetwork([[1,2,3], [3,2,1], [1,4,1], [5,1,3]], 6, 5, 20)
network.process_self_organization()