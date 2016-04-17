'''
Created on Oct 4, 2014

@author: sunnycomes
'''

from tornado.options import options
from tornado.web import RequestHandler

from src.common.post_parser import BasicParser
from src.common.settings import get_site_info, get_3rd_party_snippet

class PostHandler(RequestHandler):
    '''
    This handler is used to deal with the requests for single post page.
    Visiting url is http://localhost:9999/post_name.html
    '''
    def get(self):
        uri = self.request.uri
        post_name = uri.split("/")[2].replace("html", 'markdown')

        post = BasicParser.parse(options.posts_dir, post_name)
        if post_name and post_name.endswith('.pdf'):
            self.set_header("Content-Type", 'application/pdf; charset="utf-8"')
            self.write(post)
        elif post_name and post_name.endswith('.markdown'):
            params = get_site_info()
            snippets = get_3rd_party_snippet()
            template_file_name = "post.html"
            self.render(template_file_name, post = post, params = params, snippets = snippets)

handler = (r"/post/.*", PostHandler)
