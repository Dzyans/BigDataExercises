# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:07:42 2017

@author: s123725
"""
import sys
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class OccurencesCount(MRJob):
    """
    def mapper(self,  _, line):
        yield 'chars', len(line)
        yield 'words', len(line.split())
        yield 'lines', 1
    
    def reducer(self, key, values):
        yield key, sum(values)
    """
    def init_get_words(self):
        self.words = {}

    def get_words(self, _, line):
        for word in WORD_RE.findall(line):
            word = word.lower()
            self.words.setdefault(word, 0)
            self.words[word] = self.words[word] + 1

    def final_get_words(self):
        for word, val in self.words.iteritems():
            yield word, val

    def sum_words(self, word, counts):
        yield word, sum(counts)

    def steps(self):
        return [MRStep(mapper_init=self.init_get_words,
                       mapper=self.get_words,
                       mapper_final=self.final_get_words,
                       combiner=self.sum_words,
                       reducer=self.sum_words)]
    
if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print "Program requires path to file for reading!"
        sys.exit(1)
    OccurencesCount.run()