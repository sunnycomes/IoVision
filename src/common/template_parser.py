'''
Created on Oct 6, 2014

@author: sunnycomes
'''

from tornado import template


class TemplateParser(object):
    '''
    This TemplateParser is a util class dedicated to parse html template files
    '''

    @staticmethod
    def parse(dirx, file_name, **params):
            t = template.Loader(dirx)
            return t.load(file_name).generate(**params)