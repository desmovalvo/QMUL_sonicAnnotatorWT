#!/usr/bin/python3

# global reqs
import logging

class ActionHandler:

    """This class is used to handle the action requests"""

    # constructor
    def __init__(self, kp):

        """Constructor of the handler"""

        # debug message
        logging.debug("ActionHandler::__init__() invoked")
        

    def handle(self, added, removed):

        """This method is triggered every time a notification or a ping arrives"""

        # parse the message
        logging.debug(added)
        logging.debug(removed)
        
        # debug message
        logging.debug("ActionHandler::handle() invoked")

        # TODO retrieve input of that actions
