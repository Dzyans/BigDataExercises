# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:17:41 2017

@author: tadah
"""
from mrjob.job import MRJob
from mrjob.step import MRStep
import sys
import timeit
import heapq as minq


class edgeCount(MRJob):
  heap = list()
  def steps(self):
       return [MRStep(mapper=self.mapper,  reducer = self.reducer_vertex_weight)]
  
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
  
  def reducer_vertex_weight(self, vertex, weights):
      w = sum(weights)

      if heap[0][0] < w:
        minq.heappop(heap)
        minq.heappush(heap, (w, vertex))
      
if __name__ == '__main__':
    print ("Setting up variables and initiating timer")
    start_time = timeit.default_timer()
    heap = [(0, ("",""))] * 10
    minq.heapify(heap)
    
    edgeCount.run()
    for i in range(len(heap)):
          print(minq.heappop(heap))
    elapsed = timeit.default_timer() - start_time
    sys.exit("Done parsing in " + str(elapsed) + " seconds")
      