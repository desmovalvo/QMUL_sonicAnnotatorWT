# SonicAnnotator WT

## Introduction

This project contains the WebThing of the Sonic Annotator tool. Starting this tool,
a new WebThing will be created, that put into SEPA its Thing Description.
The WebThing will then subscribe to Action Requests, in order to get notification
about new requests. The handler will then execute the action and put the results
into SEPA.

## Quick start

To start the web thing simply type:

```bash
$ python3 annotatorWT.py
```

Remember to edit its configuration from `annotator.jsap`.

## Basic Behaviour

The WebThing pushes its Thing Description into a running instance of SEPA. The Thing Description states all the properties, events and actions exposed by the Thing.
Then the WebThing subscribes to all the action requests addressed to it. The handler read all of the data contained in the request, performs the audio analysis and return the results.

## What you should NOT expect right now

This code is currently a draft, mainly oriented at a demonstrating the basic SEPA WoT interaction scheme. So, currently part of the request parameters are hardcoded and will be soon replaced by a dynamic retrieval of their values. We currently interact with vampy, not with sonic annotator that will require a further work.

## License

This software is released with GNU GPL v3.0. 
