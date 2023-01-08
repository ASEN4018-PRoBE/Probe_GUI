from Storage import Storage
from interfaces import DMMInterface, ISOInterface, MCUInterface

class Tester:
    def __init__(self, test_config):
        self.test_config = test_config
        self.test_storage = Storage(test_config) # to be populated