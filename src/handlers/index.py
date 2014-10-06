'''
Created on Oct 4, 2014

@author: sunnycomes
'''

from tornado.web import url, RequestHandler
from src.common.markdown_parser import getAllParsedPosts
from src.common.settings import getSiteInfo

class IndexHandler(RequestHandler):
    '''
    This handler is used to deal with the requests for index page.
    Visiting url is http://localhost:9999/
    '''
    def get(self):
        posts = getAllParsedPosts()
        
        params = getSiteInfo()
        
        template_file_name = "index.html"
        self.render(template_file_name, posts = posts, params = params)

handler = url(r"/", IndexHandler)     