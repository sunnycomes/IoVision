'''
Created on Oct 6, 2014

@author: sunnycomes
'''
import os
from tornado.options import options


def get_site_info():
    params = {}
    params["author"] = options.author
    params["url"] = options.url
    params["title"] = options.title
    params["github_fork_link"] = options.github_fork_link
    params["disqus_shortname"] = options.disqus_shortname
    params["google_analytics_id"] = options.google_analytics_id
    
    return params

def get_3rd_party_snippet():
    snippets = {}
    
    dest_dir = options.global_resource_dir + os.sep + "snippet"
    disqus_file = file(dest_dir + os.sep + "disqus.snippet")
    disqus_snippet = disqus_file.read()
    snippets["disqus_snippet"] = disqus_snippet.replace("param_disqus_shortname", options.disqus_shortname)
    
    google_analytics_file = file(dest_dir + os.sep + "google_analytics.snippet")
    google_analytics_snippet = google_analytics_file.read()
    snippets["google_analytics_snippet"] = google_analytics_snippet.replace("param_google_analytics_id", options.google_analytics_id)
    
    github_fork_file = file(dest_dir + os.sep + "github_fork.snippet")
    github_fork_snippet = github_fork_file.read()
    snippets["github_fork_snippet"] = github_fork_snippet.replace("param_github_fork_link", options.github_fork_link)
    
    return snippets