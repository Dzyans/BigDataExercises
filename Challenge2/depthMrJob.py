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


class eulerGraphs(MRJob):
    def steps(self):
        return [MRStep(mapper_init=self.splitFile,
                       mapper=self.get_edges,
                       mapper_final=self.final_get_edges,
                       )]
    
    
    def splitFile(self):
        self.nodes = {}
        
    def get_edges(self, _, line):
        for node in WORD_RE.findall(line):
            
            self.nodes.setdefault(node, {})
            self.nodes[node] = self.nodes[node]     

    def final_get_edges(self):
        for node, val in self.nodes.iteritems():
            yield node, val

    def sum_edges(self, edge, counts):
        yield edge, sum(counts)    
    
    def even_edges(self, edge, counts):
        yield edge, sum(counts) % 2 == 0    
        
if __name__ == '__main__':
    eulerGraphs.run()