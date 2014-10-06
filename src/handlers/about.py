'''
Created on Oct 4, 2014

@author: sunnycomes
'''

import os
from tornado.options import options
from tornado.web import url, RequestHandler
from src.common.markdown_parser import BasicParser

class AboutHandler(RequestHandler):
    '''
    This handler is used to deal with the requests for about page.
    Visiting url is http://localhost:9999/about
    '''
    def get(self):
        full_name = "about.markdown"
        post = BasicParser.parse(options.about_dir, full_name)
        post["title"] = options.author

        params = {}
        params["author"] = options.author
        params["url"] = options.url
        params["title"] = options.title
        params["github_link"] = options.github_link
        params["disqus_shortname"] = options.disqus_shortname
        
        theme_file_path = options.theme_path + os.sep + "about.html"
        self.render(theme_file_path, post = post, params = params)

handler = url(r"/about", AboutHandler)