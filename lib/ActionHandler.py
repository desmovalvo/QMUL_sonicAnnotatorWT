#!/usr/bin/python3

# global reqs
import os
import vamp
import numpy
import logging
import librosa
import subprocess
from rdflib import *

# local reqs
from lib.utils import *

class ActionHandler:

    """This class is used to handle the action requests"""

    # constructor
    def __init__(self, kp, jsap):

        """Constructor of the handler"""

        # debug message
        logging.debug("ActionHandler::__init__() invoked")

        # working files and directories
        self.workDir = os.getcwd()
        self.n3File = self.workDir + "/lib/transform.n3"
        
        # store the kp and the jsap object
        self.jsap = jsap
        self.kp = kp
        

    def handle(self, added, removed):

        """This method is triggered every time a notification or a ping arrives"""

        # parse the message
        logging.debug(added)
        logging.debug(removed)
        
        # debug message
        logging.debug("ActionHandler::handle() invoked")

        # we need to get all data related to the action , the song name and the transform
        # TODO -- the song is currently hardcoded, since it is just for a demo;
        #         we need to retrieve the song through the websocket
        actionInstance = None
        transformUri = None
        songName = "/home/val/QMUL/code/songRepo/audio/Rein_-_Occidente.mp3"        
        
        # iterate over added building
        # TODO -- consider that we may receive multiple action requests with a notification
        #         but for the demo purposes it is not mandatory        
        for result in added:
            actionInstance = result["instance"]["value"]
            if result["fieldName"]["value"] == "transformUri":
                transformUri = result["fieldValue"]["value"]
            if result["fieldName"]["value"] == "audio":
                songName = result["fieldValue"]["value"]
                print(songName)

        # get the transform!
        # TODO - transforms specify a plugin as an URI (e.g. http://vamp-plugins.org/rdf/plugins/vamp-example-plugins#amplitudefollower)
        #        we need to find the correspondent plugin name.. It would be nice to have the existing datatype property plugin_name in
        #        the RDF configuration file of the transform
        # NOTE - we now use this query to build the n3 file to feed sonic-annotator
        #        soon the code will be split into vampWT and sonicAnnotatorWT
        status, results =  self.kp.query(self.jsap.queryUri, self.jsap.getQuery("GET_TRANSFORM_CONSTRUCT", {"transform": transformUri}))
        getN3FromBindings(results["results"]["bindings"], self.n3File)

        # start the analysis
        logging.debug("ActionHandker::handle() -- performing analysis (workDir: %s)" % self.workDir)
        subprocess.run(["sonic-annotator", "-t", self.n3File, songName, "-w", "rdf", "--rdf-basedir", self.workDir])        
        logging.debug("ActionHandker::handle() -- writing results")        

        # write data into SEPA
        # TODO -- at the moment I put something horrible.. need to fix
        print(self.jsap.getUpdate("ADD_COMPLETION_TIMESTAMP_WITH_OUTPUT", {
            "instance":actionInstance,
            "outputFieldValue": "WIP",
            "outputFieldName":"output"
        }))
