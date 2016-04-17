'''
Created on Oct 4, 2014

@author: sunnycomes
'''

from tornado.web import RequestHandler

from src.common.post_parser import get_all_parsed_posts
from src.common.settings import get_site_info, get_3rd_party_snippet

class IndexHandler(RequestHandler):
    '''
    This handler is used to deal with the requests for index page.
    Visiting url is http://localhost:9999/
    '''
    def get(self):
        posts = get_all_parsed_posts()

        params = get_site_info()

        snippets = get_3rd_party_snippet()

        template_file_name = "index.html"

        self.render(template_file_name, posts = posts, params = params, snippets = snippets)

handler = (r"/", IndexHandler)
