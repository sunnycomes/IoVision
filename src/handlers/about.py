'''
Created on Oct 4, 2014

@author: sunnycomes
'''

from tornado.options import options
from tornado.web import RequestHandler

from src.common.post_parser import BasicParser
from src.common.settings import get_site_info, get_3rd_party_snippets

class AboutHandler(RequestHandler):
    '''
    This handler is used to deal with the requests for about page.
    Visiting url is http://localhost:9999/about
    '''
    def get(self):
        uri = self.request.uri
        if uri == '/about/':
            uri = '/about/index.html'

        full_name = uri.split("/")[2].replace("html", 'markdown')
        post = BasicParser.parse(options.about_dir, full_name)

        if full_name and full_name.endswith('.pdf'):
            self.set_header("Content-Type", "application/pdf; charset=utf-8")
            self.write(post)
            return

        params = get_site_info()
        snippets = get_3rd_party_snippets()
        template_file_name = "about.html"

        self.render(template_file_name, post = post, params = params, snippets = snippets)

handler = (r"/about/.*", AboutHandler)
