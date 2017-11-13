# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:59:19 2017

@author: s123725
"""

import six
from mrjob.job import MRJob
from mrjob.step import MRStep
import json

class Finalize(MRJob):
    def steps(self):
        return [MRStep(
                mapper=self.map_leaf,
                reducer=self.find_leaf
                ),MRStep(
                mapper = self.mean_map,
                reducer = self.mean_reduce
                ),MRStep(
                mapper=self.mapper_make_counts_key,
                reducer=self.reducer_output_vertices
                )]
    
    def map_leaf(self,key,line):
        _key, _line = line.split('\t')
        foo =  json.loads(_key)
        bar = json.loads(_line)

        self.nodeid = foo[0]
        self.subreddit = foo[1]
        self.connections = bar[0]
        self.distance = bar[1]
        self.visited = bar[2]
        yield([self.nodeid,self.subreddit],[self.connections,self.distance,self.visited])    

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
        #self.increment_counter('group','mean_map_calls',1)
        yield (line[3],line[1])
    
    def mean_reduce(self,key,values):
        #self.increment_counter('group','mean_reduce',1)
        yield (key , float(sum(values)))
            
    def mapper_make_counts_key(self, key, line):
        #self.increment_counter('group','mean_map_calls',1)
        # sort by values
        yield( ['%04d' % int(line), key])

    
    def reducer_output_vertices(self, count, vertices):
        #self.increment_counter('group','mean_map_calls',1)
        # First Column is the count
        # Second Column is the word
        for vertice in vertices:
            yield count, vertice    

if __name__ == '__main__':
    Finalize.run()