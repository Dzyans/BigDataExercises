# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:17:41 2017

@author: tadah
"""
from mrjob.job import MRJob
from mrjob.step import MRStep
import sys

class edgeCount(MRJob):

    def steps(self):
        print ("The graph has an Euler tour")
            # define the steps for the job, here two steps.
        return [MRStep(mapper=self.mapper,
                reducer=self.reducer_vertex_links)]
  
  #### FIRST JOB ####
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
      
    if __name__ == '__main__':
        edgeCount.run()
        sys.exit("The graph does hot have an Euler tour")
  
 #### SECOND JOB ####
def reducer_uneven_links(self, _, vertex_counts):
  # check if any of the vertices have uneven degrees.
  
  if __name__ == '__main__':
      edgeCount.run()
      sys.exit("The graph does hot have an Euler tour")
      