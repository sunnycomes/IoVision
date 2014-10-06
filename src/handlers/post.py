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
    Visiting url is http://localhost:6666/post?name=post_name
    '''
    def get(self):
        post_name = self.get_arguments("name", True)
        full_name = post_name[0] + ".markdown"
        post = BasicParser.parse(options.posts_dir, full_name)
        
        params = {}
        params["author"] = options.author
        params["url"] = options.url
        params["title"] = options.title
        params["github_link"] = options.github_link
        params["disqus_shortname"] = options.disqus_shortname
        
        template_file_path = options.current_template_dir + os.sep + "post.html"
        self.render(template_file_path, post = post, params = params)

handler = url(r"/post/*", PostHandler)