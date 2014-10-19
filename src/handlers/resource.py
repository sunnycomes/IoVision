'''
Created on Oct 4, 2014

@author: sunnycomes
'''

from tornado.options import options
from tornado.web import  StaticFileHandler

class ResourceHandler(StaticFileHandler):
    '''
    This handler is used to deal with the requests for resource, such as images or plain text files.
    Visiting url is http://localhost:9999/res/item_path, item_path is the path relative to global_resource_dir
    '''
    
    def initialize(self, path=None):
        uri_path = self.request.uri
        rel_path = "/".join(uri_path.split("/")[2:-1])
        super(ResourceHandler, self).initialize(options.global_resource_dir, rel_path)
        
    @classmethod
    def get_absolute_path(cls, root, path):
        return StaticFileHandler.get_absolute_path(root, "")

    def get(self):
        super(ResourceHandler, self).get("")

handler = (r"/res/.*", ResourceHandler)