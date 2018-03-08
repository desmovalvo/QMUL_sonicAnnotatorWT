#!/usr/bin/python3

# global reqs
import logging
from uuid import uuid4
from sepy.JSAPObject import *
from sepy.LowLevelKP import *

# the class
class Device:

    """This class represents a generic WebThing"""
    
    # constructor
    def __init__(self, jsap, thingName):

        """This method is used to initialize the WebThing.
        Mandatory parameters are the name of the JSAP file
        with the configuration and the name of the WebThing 
        to create"""
        
        # debug message
        logging.debug("Device::__init__() invoked")

        # read the jsap provided
        logging.debug("Device::__init__() -- Reading configuration file")
        self.jsap = JSAPObject(jsap)

        # setting a namespace
        self.defaultNS = "http://eecs.qmul.ac.uk/wot#"
        
        # store things data
        self.thingID = str(uuid4())
        self.thingName = thingName
        self.thingURI = self.defaultNS + self.thingID
        
        # initialize an empty dictionary for events, props and actions
        # keys are represented by names, values are the related URIs
        self.events = {}
        self.actions = {}
        self.properties = {}
        
        # create a KP
        logging.debug("Device::__init__() -- Creating a new KP")
        self.kp = LowLevelKP(None, 10)

        # save the update uri
        self.updateURI = self.jsap.updateUri
        
        # call TD_INIT
        u = self.jsap.getUpdate("ADD_NEW_THING", {
            "name": self.thingName,
            "thing": self.thingURI
        })
        self.kp.update(self.updateURI, u)

        
    def addProperty(self):
        logging.error("Device::addProperty yet to implement!")

        
    # add new action
    def addAction(self, actionName, actionURI=None):

        """This method is used to put the description of
        an action into the SEPA instance. Mandatory is the
        name of the action to publish. The eventURI is instead
        optional. If not provided, will be automatically generated"""

        # debug message
        logging.debug("Debug::addAction() invoked")

        # generate an URI and store data
        if not actionURI:
            self.actions[actionName] = str(uuid4())
        else:
            self.actions[actionName] = actionURI
        
        # generate and perform the update
        u = self.jsap.getUpdate("ADD_NEW_ACTION", {
            "thing": self.thingURI,
            "action": "---",
            "newName": "---",
            "newInDataSchema": "---",
            "newOutDataSchema": "---"
        })
        self.kp.update(self.updateURI, u)


    # add event
    def addEvent(self, eventName, eventURI=None):

        """This method is used to put the description of
        an event into the SEPA instance. Mandatory is the
        name of the event to publish. The eventURI is instead
        optional. If not provided, will be automatically generated"""
        
        # debug message
        logging.debug("Device::addEvent() invoked")
        
        # generate an URI and store data
        if not eventURI:
            self.events[eventName] = str(uuid4())
        else:
            self.events[eventName] = eventURI

        # generate and perform the update
        u = self.jsap.getUpdate("ADD_EVENT", {
            "event": self.events[eventName],
            "thing": self.thingURI,
            "eName": eventName,
            "outDataSchema": "-"
        })
        self.kp.update(self.updateURI, u)
        
        
    def subscribeToAction(self):
        logging.error("Device::subscribeToAction yet to implement!")


    # delete Web Thing
    def deleteWT(self):

        """This method is used to delete a Thing from the KB. It should be
        called before shutting down the Thing"""

        # debug message
        logging.debug("Device::deleteWT() invoked")
        
        # delete properties
        # delete actions
        logging.debug("Device::deleteWT() -- removing all the actions")
        for a in self.actions:
            u = self.jsap.getUpdate("DELETE_ACTION", {
                "thing": self.thingURI,
                "action": self.actions[a]
            })
            self.kp.update(self.updateURI, u)        
        
        # delete events
        logging.debug("Device::deleteWT() -- removing all the events")
        for e in self.events:
            u = self.jsap.getUpdate("DELETE_EVENT", {
                "thing": self.thingURI,
                "event": self.events[e]
            })
            self.kp.update(self.updateURI, u)
        
        # delete thing
        logging.debug("Device::deleteWT() -- removing thing")
        u = self.jsap.getUpdate("DELETE_THING", {
            "thing": self.thingURI })
        self.kp.update(self.updateURI, u)    
