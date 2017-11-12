# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:17:41 2017

@author: tadah
"""
from mrjob.job import MRJob
from mrjob.step import MRStep
import sys
import numpy as np
import heapq as minq


class edgeCount(MRJob):

  def steps(self):
       return [MRStep(mapper_init=self.init, mapper=self.mapper, reducer=self.reducer_vertex_links), MRStep(mapper=self.top_10_mapper, reducer=self.top_10_reducer, reducer_final = self.final)]
  
  #### FIRST JOB ####
  def init(self):
        top_ten_weights = [0] * 10
        self.heap = minq.heapify(top_ten_weights)
        
  
  def mapper(self, _, line):
        line.strip()    
        sbr_ids = line.split()
        #count_sbr_ids = len(sbr_ids)
        counter = 0
        
        for sbr_id in sbr_ids:
            cur_sbr_id = sbr_id
            #for each element in the line, yield the vertex and 1
            for next_sbr_id in sbr_ids[counter:]: 
                vertex = cur_sbr_id + " " + next_sbr_id
            
                yield (vertex, 1)
            counter = counter + 1    
  
  def reducer_vertex_links(self, vertex, counts):
        # sum occurences (equal to degree) of the vertex
        yield (vertex,sum(counts))
  
  def top_10_mapper(self, vertex, vertex_weight):
           
        ##check if weight is below current lowest top 10
        if vertex_weight > self.heap[0]:
            yield (vertex, vertex_weight)
        
                
                
        
  def top_10_reducer(self, vertex, vertex_weight):
      
      self.heap.push(self.heap, vertex_weight)
        # check if any of the vertices have uneven degrees.

  def final(self, _, heap):
      for val in self.heap:          
          yield self.heap.pop()
      
if __name__ == '__main__':
    edgeCount.run()
    
    sys.exit("The graph does hot have an Euler tour")
      