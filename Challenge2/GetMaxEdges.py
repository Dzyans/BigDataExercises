# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:17:41 2017

@author: tadah
"""
from mrjob.job import MRJob
from mrjob.step import MRStep
import sys

import heapq as minq


class edgeCount(MRJob):
  heap = list()
  def steps(self):
       return [MRStep(mapper=self.mapper, combiner=self.combine_edge_weight, reducer = self.reducer_vertex_weight), MRStep(reducer = self.reducer_find_max_word, reducer_init = self.init)]#,MRStep(mapper_init = self.init, mapper_final = self.final, mapper = self.reducer_vertex_weight)]
  
  #### FIRST JOB ####
  def init(self):
        print ("init reducer")
        self.final_counter = 0
        self.heap = [(0, "")] * 10
        minq.heapify(self.heap)
  
  def mapper(self, _, line):
        line.strip()    
        sbr_ids = line.split()
        #count_sbr_ids = len(sbr_ids)
        counter = 1
        
        for sbr_id in sbr_ids:
            cur_sbr_id = sbr_id
            #for each element in the line, yield the vertex and 1
            for next_sbr_id in sbr_ids[counter:]: 
                if next_sbr_id > cur_sbr_id:
                    vertex = cur_sbr_id +" "+ next_sbr_id
                else:
                    vertex = next_sbr_id +" "+ cur_sbr_id
            
                yield (vertex, 1)
            counter = counter + 1    
        #print("mapper done")
  def combine_edge_weight(self, vertex, counts):
        # sum occurences (equal to degree) of the vertex
        #weight = sum(counts)
        yield (vertex, sum(counts))
 
    
  def reducer_vertex_weight(self, vertex, weights):
     yield None, (sum(weights), vertex)
     
      #yield (vertex, sum(weights))
      
  def reducer_find_max_word(self, _, word_count_pairs):
        print("final reducer") 
        print(len(heap))
      # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        yield max(word_count_pairs)

  #def reducer_find_max_common_authors(self, _, word_count_pairs):
   #   yield (_, sum(word_count_pairs)
      #print(word_count_pairs) 
      #if self.heap[0] < word_count_pairs:
        #  self.heap.pop()
        #  self.heap.push(self.heap, word_count_pairs)
        #  yield (word_count_pairs)
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        

  #def reduce_to_max(self, _, weight_pairs):
       
     # yield (weight_pairs, "")
      
    
    #def top_10_mapper(self, vertex, vertex_weight):
           
        ##check if weight is below current lowest top 10
     #   if vertex_weight > self.heap[0]:
      #      yield (vertex, vertex_weight)
       
  #def top_10_reducer(self, vertex, vertex_weight):
      
   #   self.heap.push(self.heap, vertex_weight)
        # check if any of the vertices have uneven degrees.

  #def final(self, _, heap):
   #   for val in self.heap:          
    #      yield self.heap.pop()
      
if __name__ == '__main__':
    print ("init reducer")
    final_counter = 0
    heap = [(0, "")] * 10
    minq.heapify(heap)
    
    edgeCount.run()
   
    sys.exit("The graph does hot have an Euler tour")
      