#!/usr/bin/python3

# config
CONFIG_FILE = "annotator.jsap"
SONIC_ANN = ["sonic-annotator", "-l"]

# global reqs
import time
import vamp
import logging
import subprocess
from sepy.JSAPObject import *

# local reqs
from lib.Device import *
from lib.ActionHandler import *

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
    plugins = subprocess.check_output(SONIC_ANN)
    for plugin in vamp.list_plugins():
        wt.addAction(plugin)
                
    # 6 - start a ping generator thread
    wt.waitForActions(ActionHandler)
    
    # 7 - subscribe to action requests

    # 8 - wait, then destroy data
    try:
        input("Press <ENTER> to close the WebThing")
        logging.debug("Closing WebThing")
        wt.deleteWT()
    except KeyboardInterrupt:
        logging.debug("Closing WebThing")
        wt.deleteWT()
