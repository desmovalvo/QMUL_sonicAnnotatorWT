#!/usr/bin/python3

# global reqs
from rdflib import *

def getN3FromBindings(bindings, filename):

    """This function is used to write an N3 file from
    bindings obtained with a SPARQL CONSTRUCT query"""

    # init an empty graph
    g = Graph()

    # iterate over bindings
    for binding in bindings:
    
        # subject
        s = None
        if binding["subject"]["type"] == "uri":
            s = URIRef(binding["subject"]["value"])
        else:
            s = BNode(binding["subject"]["value"])
            
        # predicate
        p = None
        if binding["predicate"]["type"] == "uri":
            p = URIRef(binding["predicate"]["value"])
        else:
            p = BNode(binding["predicate"]["value"])
        
        # object
        o = None
        if binding["object"]["type"] == "uri":
            o = URIRef(binding["object"]["value"])
        elif binding["object"]["type"] == "litearl":
            o = Literal(binding["object"]["value"])
        else:
            o = BNode(binding["object"]["value"])
        
        # triple
        g.add((s,p,o))

    # write the n3 file
    g.serialize(destination=filename, format='n3')
