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
                       combiner=self.sum_edges,
                       reducer=self.even_edges
                       )]
    
    
    def splitFile(self):
        self.edges = {}
        
    def get_edges(self, _, line):
        for edge in WORD_RE.findall(line):
            self.edges.setdefault(edge, 0)
            self.edges[edge] = self.edges[edge] + 1

    def final_get_edges(self):
        for edge, val in self.edges.iteritems():
            yield edge, val

    def sum_edges(self, edge, counts):
        yield edge, sum(counts)    
    
    def even_edges(self, edge, counts):
        yield edge, sum(counts) % 2 == 0    
        
if __name__ == '__main__':
    eulerGraphs.run()