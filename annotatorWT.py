#!/usr/bin/python3

# config
CONFIG_FILE = "annotator.jsap"

# global reqs
import logging
from sepy.JSAPObject import *

# local reqs
from lib.Device import *

# main
if __name__ == "__main__":

    # initialize the logging system
    logger = logging.getLogger('annotatorWT')
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)
    logging.debug("Logging subsystem initialized")

    # 1 - create an instance of the Device
    wt = Device(CONFIG_FILE, "SonicAnnotatorWT")

    # 2 - specify properties
    wt.addProperty()

    # 3 - specify events
    wt.addEvent("Ping")

    # 4 - specify actions
    wt.addAction()    
    
    # 6 - start a ping generator thread
    # 7 - subscribe to action requests
    # 8 - wait, then destroy data
