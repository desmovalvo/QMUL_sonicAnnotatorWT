#!/usr/bin/python3

# global reqs
import vamp
import numpy
import logging
import librosa

class ActionHandler:

    """This class is used to handle the action requests"""

    # constructor
    def __init__(self, kp, jsap):

        """Constructor of the handler"""

        # debug message
        logging.debug("ActionHandler::__init__() invoked")

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
        actionName = None
        actionUri = None
        songName = "/home/val/QMUL/code/songRepo/audio/Rein_-_Occidente.mp3"        
        
        # iterate over added building
        # TODO -- consider that we may receive multiple action requests with a notification
        #         but for the demo purposes it is not mandatory        
        for result in added:

            # get the action name
            actionURI = result["action"]["value"]
            actionName = result["actionName"]["value"]
            actionInstance = result["instance"]["value"]

            # get the parameters
            # TODO -- for demo purposes we will use default values and a default song
               
        # TODO retrieve input of that actions
        logging.debug("ActionHandker::handle() -- loading audio file")
        data, rate = librosa.load(songName)
        logging.debug("ActionHandker::handle() -- performing analysis with " + actionName)
        c = vamp.collect(data, rate, actionName)
        print(str(c))
        logging.debug("ActionHandker::handle() -- writing results")        

        # sanitize output
        outString = str(c).replace("\n", "").replace("\r", "").replace("'", "").replace('"', '')
        
        # TODO -- put data into SEPA

        print(self.jsap.getUpdate("ADD_COMPLETION_TIMESTAMP_WITH_OUTPUT", {
            "instance":actionInstance,
            "outputFieldValue": outString,
            "outputFieldName":"output"
        }))
        
        self.kp.update(self.jsap.updateUri, self.jsap.getUpdate("ADD_COMPLETION_TIMESTAMP_WITH_OUTPUT", {
            "instance":actionInstance,
            "outputFieldValue": outString,
            "outputFieldName":"output"
        }))
