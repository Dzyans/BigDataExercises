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
from collections import defaultdict

WORD_RE = re.compile(r"[\w']+")
globvar  = 0

def set_globvar(length):
    global globvar 
    globvar = length    # Needed to modify global copy of globvar

class Graphs(MRJob):
    def steps(self):
        return [MRStep( 
                mapper=self.get_vertex,
                combiner=self.combine_vertices,
                reducer=self.reduce_vertices
                ), 
                MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                mapper=self.map_graph,
                reducer= self.reducer_graph
                ),MRStep(
                reducer=self.find_leaf
                ),MRStep(
                mapper = self.mean_map,
                reducer = self.mean_reduce
                ),MRStep(
                mapper=self.mapper_make_counts_key,
                reducer=self.reducer_output_vertices
                )]       
    def get_vertex(self, key, line):
        subreddit, vertex, parent = line.split()
        yield ([vertex,subreddit] , parent)
    
    def combine_vertices(self,vertices,parents):
        for parent in parents:
            yield (vertices, parent)
        
    def reduce_vertices(self, vertices, parents):
        yield (vertices, [list(parents),0,'White'])
        
    def map_graph(self, key, line):
        self.nodeid = key[0]
        self.subreddit = key[1]
        self.connections = line[0]
        self.distance = 0
        self.visited = 'White'
        if('t3_' in self.nodeid and self.visited != 'Black'):
            self.visited = 'Gray'
        if(self.visited == 'Gray'):
            for connection in self.connections:
                yield (connection, int(self.distance) +1)
                yield (connection, 'Gray')
                yield (connection,self.subreddit)
            self.visited = 'Black'
        yield (self.nodeid, self.distance)
        yield (self.nodeid, self.visited)
        yield(self.nodeid, self.connections)
        yield(self.nodeid, self.subreddit)
        
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
    
    def find_leaf(self,key,values):
        for value in values:
            nodeid = key[0]
            subreddit = key[1]
            connections = value[0]
            distance = value[1]
            visited = value[2]
        if(visited=='Black' and len(connections) == 0):
            yield(nodeid,[connections,distance,visited,subreddit])    
        # Step 2
       
    def mean_map(self,key,line):
        self.increment_counter('group','mean_map_calls',1)
        set_globvar(globvar +1)
        yield (line[3],line[1])
    
    def mean_reduce(self,key,values):
        self.increment_counter('group','mean_reduce',1)
        yield (key , float(sum(values)))
            
    def mapper_make_counts_key(self, key, line):
        self.increment_counter('group','mean_map_calls',1)
        # sort by values
        yield( ['%04d' % int(line), key])

    
    def reducer_output_vertices(self, count, vertices):
        self.increment_counter('group','mean_map_calls',1)
        # First Column is the count
        # Second Column is the word
        for vertice in vertices:
            yield count, vertice        
class finalize:
    def steps(self):
        return [MRStep(
                reducer=self.find_leaf
                ),MRStep(
                mapper = self.mean_map,
                reducer = self.mean_reduce
                ),MRStep(
                mapper=self.mapper_make_counts_key,
                reducer=self.reducer_output_vertices
                )]
    def find_leaf(self,key,values):
        for value in values:
            nodeid = key[0]
            subreddit = key[1]
            connections = value[0]
            distance = value[1]
            visited = value[2]
        if(visited=='Black' and len(connections) == 0):
            yield(nodeid,[connections,distance,visited,subreddit])    
        # Step 2
       
    def mean_map(self,key,line):
        self.increment_counter('group','mean_map_calls',1)
        set_globvar(globvar +1)
        yield (line[3],line[1])
    
    def mean_reduce(self,key,values):
        self.increment_counter('group','mean_reduce',1)
        yield (key , float(sum(values)))
            
    def mapper_make_counts_key(self, key, line):
        self.increment_counter('group','mean_map_calls',1)
        # sort by values
        yield( ['%04d' % int(line), key])

    
    def reducer_output_vertices(self, count, vertices):
        self.increment_counter('group','mean_map_calls',1)
        # First Column is the count
        # Second Column is the word
        for vertice in vertices:
            yield count, vertice    

if __name__ == '__main__':
    Graphs.run()