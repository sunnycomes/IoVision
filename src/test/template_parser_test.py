'''
Created on Oct 6, 2014

@author: sunnycomes
'''
import os
from src.common.markdown_parser import BasicParser
from src.common import template_parser

if __name__ == '__main__':
    params = {}
    params["author"] = "options.author"
    params["url"] = "options.url"
    params["title"] = "options.title"
    params["github_link"] = "options.github_link"
    params["disqus_shortname"] = "options.disqus_shortname"
    
    post = BasicParser.parse(os.getcwd() + os.sep + "resources", "2014-03-1-talk-about-bitcoin-change.markdown")
    
    path = os.getcwd() + os.sep + "resources"
    
    file_name = "post.html"
    
    html = template_parser.TemplateParser.parse(path, file_name, post=post, params=params)
    print html