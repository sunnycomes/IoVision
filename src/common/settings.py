'''
Created on Oct 6, 2014

@author: sunnycomes
'''

from tornado.options import options

def get_site_info():
    params = {}
    params["author"] = options.author
    params["url"] = options.url
    params["title"] = options.title
    params["github_link"] = options.github_link
    params["disqus_shortname"] = options.disqus_shortname
    params["google_analytics_id"] = options.google_analytics_id
    
    return params