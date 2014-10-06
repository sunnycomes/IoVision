'''
Created on Oct 6, 2014

@author: sunnycomes
'''

from tornado.options import options

def getSiteInfo():
    params = {}
    params["author"] = options.author
    params["url"] = options.url
    params["title"] = options.title
    params["github_link"] = options.github_link
    params["disqus_shortname"] = options.disqus_shortname
    
    return params