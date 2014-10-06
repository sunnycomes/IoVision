'''
Created on Oct 4, 2014

@author: sunnycomes
'''

from tornado.options import options
from tornado.web import url, RequestHandler
from src.common.markdown_parser import BasicParser
from src.common.settings import getSiteInfo

class PostHandler(RequestHandler):
    '''
    This handler is used to deal with the requests for single post page.
    Visiting url is http://localhost:6666/post?name=post_name
    '''
    def get(self):
        uri = self.request.uri
        post_name = uri.split("/")[2]
        full_name = post_name.split(".")[0] + ".markdown"
        post = BasicParser.parse(options.posts_dir, full_name)
        
        params = getSiteInfo()
        
        template_file_name = "post.html"
        self.render(template_file_name, post = post, params = params)


handler = url(r"/post/.*", PostHandler)