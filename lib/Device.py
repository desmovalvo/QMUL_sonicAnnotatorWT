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
        logging.debug("Device::__init__> invoked")

        # read the jsap provided
        logging.debug("Device::__init__> Reading configuration file")
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
        logging.debug("Device::__init__> Creating a new KP")
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

    def addAction(self):
        logging.error("Device::addAction yet to implement!")


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
