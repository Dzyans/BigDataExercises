# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:15:24 2017

@author: s123725
"""

from mrjob.job import MRJob
from mrjob.util import bash_wrap
from mrjob.step import MRStep


class bashJob(MRJob):
    
    #OUTPUT_PROTOCOL = JSONValueProtocol

    def mapper_cmd(self):
        return bash_wrap("grep 'i' | wc -l ")

if __name__ == '__main__':
    bashJob().run()