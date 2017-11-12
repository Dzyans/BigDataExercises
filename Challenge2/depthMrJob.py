# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 16:19:35 2017

@author: s123725
"""

# -*- coding: utf-8 -*-

import six
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")
    
class Graphs(MRJob):
    def steps(self):
        return [MRStep( 
                mapper=self.get_vertex,
                combiner=self.combine_vertices,
                reducer=self.reduce_vertices
                ), MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ), MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                )]
    
    def init_map(self):
        self.nodeid = ''
        self.connections =  []
        #self.distance = 9999
        #self.color = 'WHITE'


    def get_vertex(self, key, line):
        vertex, parent = line.split()
        yield (vertex , parent)
    
    def combine_vertices(self,vertices,parents):
        for parent in parents:
            yield (vertices, parent)
        
    def reduce_vertices(self, vertices, parents):
        yield (vertices, [list(parents),0,'White'])
        
        
    def map_graph(self, key, line):
        self.nodeid = key
        self.connections = line[0]
        self.distance = line[1]
        self.visited = line[2]
        #print self.nodeid, self.connections, self.distance, self.visited
        if('t3_' in self.nodeid and self.visited != 'Black'):
            self.visited = 'Gray'
        if(self.visited == 'Gray'):
            for connection in self.connections:
                yield (connection, int(self.distance) +1)
                yield (connection, 'Gray')
            self.visited = 'Black'
        yield (self.nodeid, self.distance)
        yield (self.nodeid, self.visited)
        yield(self.nodeid,self.connections)
        
    def reducer_graph(self, key, values):
        edges = []
        visited = ''
        distance = 0
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
        yield(key,[edges,distance,visited])

if __name__ == '__main__':
    Graphs.run()