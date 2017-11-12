# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 16:19:35 2017

@author: s123725
"""

# -*- coding: utf-8 -*-

import sys
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")
    
class Graphs(MRJob):
    def steps(self):
        return [MRStep( 
                mapper=self.get_vertex,
                combiner=self.combine_vertices
            ), MRStep(
                mapper_init= self.init_map,
                mapper=self.map_graph,
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
        yield (vertices, list(parents))
        
    def reduce_vertices(self, vertex, parent):
        yield (vertex, parent.extend(parent))   
    
    def map_graph(self, key, line):
        
        self.nodeid = key
        self.connections = line
        self.distance = 0
        self.visited = 'WHITE'
        for connection in self.connections:
            yield (connection, int(self.distance) +1)
        yield(self.nodeid,self.connections)
    
if __name__ == '__main__':
    Graphs.run()