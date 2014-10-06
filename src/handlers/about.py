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

        theme_file_path = options.theme_path + os.sep + "about.html"
        self.render(theme_file_path, author=options.author, url=options.url, title=options.title, github_link=options.github_link, post = post)

handler = url(r"/about", AboutHandler)