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

## License

This software is released with GNU GPL v3.0. 