'''
Created on Oct 4, 2014

@author: sunnycomes
'''

from tornado.options import options
from tornado.web import url, RequestHandler
from src.common.markdown_parser import BasicParser
from src.common.settings import get_site_info, get_3rd_party_snippet

class AboutHandler(RequestHandler):
    '''
    This handler is used to deal with the requests for about page.
    Visiting url is http://localhost:9999/about
    '''
    def get(self):
        full_name = "about.markdown"
        post = BasicParser.parse(options.about_dir, full_name)
        post["title"] = options.author

        params = get_site_info()
        
        snippets = get_3rd_party_snippet()
                
        template_file_name = "about.html"
        self.render(template_file_name, post = post, params = params, snippets = snippets)

handler = (r"/about", AboutHandler)