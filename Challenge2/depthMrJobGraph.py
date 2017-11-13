# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:15:44 2017

@author: s123725
"""
import six
from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class Graphs(MRJob):
    
    def steps(self):
        return [MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                )] 
                  
    def map_graph(self, key, line):
        _key, _line = line.split('\t')
        foo =  json.loads(_key)
        bar = json.loads(_line)

        nodeid = foo[0]
        subreddit = foo[1]
        connections = bar[0]
        distance = bar[1]
        visited = bar[2]
        if('t3_' in nodeid and visited != 'Black'):
            visited = 'Gray'
        if(visited == 'Gray'):
            for connection in connections:
                yield (connection, int(distance) +1)
                yield (connection, 'Gray')
                yield (connection,subreddit)
            visited = 'Black'
        yield (nodeid, distance)
        yield (nodeid, visited)
        yield(nodeid, connections)
        yield(nodeid, subreddit)
        
    def reducer_graph(self, key, values):
        edges = []
        visited = 'White    '
        distance = 0
        subreddit = 'default value'
        # Extend new list of edges to node
        for value in values:
             if(type(value) is list and len(value) > 0):
                 edges.extend(value)
                 #yield(key, edges)
             elif(type(value) is int):
                 distance = value
                 #yield (key, distance)
             elif(isinstance(value, six.string_types) and value == 'Black'):
                 visited = 'Black'
                 #yield (key, visited)
             elif(isinstance(value, six.string_types) and value == 'Gray'):
                 visited = 'Gray'
                 #yield (key, visited)
             elif(isinstance(value,six.string_types) and 't5_' in value):
                 subreddit=value
        yield([key,subreddit],[edges,distance,visited])
    
if __name__ == '__main__':
    Graphs.run()