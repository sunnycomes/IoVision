'''
Created on Oct 4, 2014

@author: sunnycomes
'''

import os
from tornado.options import options
from tornado.web import url, RequestHandler
from src.common.markdown_parser import BasicParser

class PostHandler(RequestHandler):
    '''
    This handler is used to deal with the requests for single post page.
    Visiting url is http://localhost:6666/post/xxx
    '''
    def get(self):
        post_name = self.get_arguments("name", True)
        full_name = post_name[0] + ".markdown"
        post = BasicParser.parse(options.posts_dir, full_name)
        
        theme_file_path = options.theme_path + os.sep + "post.html"
        self.render(theme_file_path, author=options.author, url=options.url, title=options.title, post = post)

handler = url(r"/post/*", PostHandler)