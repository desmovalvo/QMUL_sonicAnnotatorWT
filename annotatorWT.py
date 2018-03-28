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

    # 1 - create an instance of the Device and one of the JSAP
    wt = Device(CONFIG_FILE, "SonicAnnotatorWT")
    jsap = JSAPObject(CONFIG_FILE, 40)

    # 2 - specify properties
    # NOTE: our thing must expose the list of plugins.
    #       we do it through an rfd:Bag.. so to addProperty
    #       we give the URI of a Bag. Then we fill it.
    bagUri = wt.getRandomURI()
    propUri = wt.getRandomURI()
    wt.addProperty(True, "hasPlugin", bagUri, propUri, "rdf:Bag")
    for plugin in vamp.list_plugins():
        wt.addCustomStatement(" <%s> rdf:li '%s' " % (bagUri, plugin))
        break
    
    # 3 - specify events
    wt.addEvent("Ping")

    # 4 - specify actions
    plugins = subprocess.check_output(SONIC_ANN)
    wt.addAction("invokeSonicAnnotator", None, [
        {"fieldName":"transform", "fieldType": jsap.namespaces["ac"] + "Transform"},
        {"fieldName":"audio", "fieldType": jsap.namespaces["rdfs"] + "Resource"}
    ])
     
    # 6 - start a ping generator thread
    # TODO - at the moment we do not need keep-alive service

    # 7 - subscribe to action requests
    wt.waitForActions(ActionHandler)
    
    # 8 - wait, then destroy data
    logging.info("WebThing ready! Waiting for actions!")
    try:
        input("Press <ENTER> to close the WebThing")
        logging.debug("Closing WebThing")
        wt.deleteWT()
    except KeyboardInterrupt:
        logging.debug("Closing WebThing")
        wt.deleteWT()
