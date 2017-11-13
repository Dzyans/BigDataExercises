# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:07:26 2017

@author: s123725
"""
from mrjob.job import MRJob
from mrjob.step import MRStep

class Prep(MRJob):
    def steps(self):
        return [MRStep( 
            mapper=self.get_vertex,
            combiner=self.combine_vertices,
            reducer=self.reduce_vertices
            )]
    def get_vertex(self, key, line):
        subreddit, vertex, parent = line.split()
        yield ([vertex,subreddit] , parent)
    
    def combine_vertices(self,vertices,parents):
        for parent in parents:
            yield (vertices, parent)
        
    def reduce_vertices(self, vertices, parents):
        yield (vertices, [list(parents),0,'White'])

if __name__ == '__main__':
    Prep.run()