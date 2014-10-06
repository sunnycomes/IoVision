'''
Created on Oct 4, 2014

@author: sunnycomes
'''

import os
from tornado.options import options
from tornado.web import url, RequestHandler
from src.common.markdown_parser import BasicParser

class IndexHandler(RequestHandler):
    '''
    This handler is used to deal with the requests for index page.
    Visiting url is http://localhost:9999/
    '''
    def get(self):
        posts = []
        post_name_list = os.listdir(options.posts_dir)
        post_name_list.sort(reverse=True)
        
        for post_name in post_name_list:
            post = BasicParser.parse(options.posts_dir, post_name)
            post["content"] = BasicParser.getBriefContent(post["content"])
            posts.append(post)
        
        theme_file_path = options.theme_path + os.sep + "index.html"
        self.render(theme_file_path, author=options.author, url=options.url, title=options.title, github_link=options.github_link, posts = posts)

handler = url(r"/", IndexHandler)     