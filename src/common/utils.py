'''
Created on Oct 6, 2014

@author: sunnycomes
'''
import ConfigParser
import os, sys
from tornado.options import define, options

def set_author(author):
    define("author", default=author, help="Author of the project")

def set_url(url):
    define("url", default=url, help="Author's home page url")

def set_title(title):
    define("title", default=title, help="Site's title")

def set_keywords(keywords):
    define("keywords", default=keywords, help="Site's keywords")

def set_description(description):
    define("description", default=description, help="Site's description")

def set_github_fork_link(link):
    define("github_fork_link", default=link, help="Github source code link")

def set_disqus_shortname(name):
    define("disqus_shortname", default=name, help="Disqus shortname used to identify the site.")

def set_google_analytics_id(idx):
    define("google_analytics_id", default=idx, help="Google analytics id used to identify this site.")

def set_port(port):
    define("port", default=port, help="the port tornado listen to")

def set_source_dir(dirx):
    define("source_dir", default=os.getcwd() + os.sep + dirx, help="Source files directory")

def set_build_dir(dirx):
    define("build_dir", default=os.getcwd() + os.sep + dirx, help="Built files directory")

def set_post_dir(dirx):
    define("posts_dir", default=options.source_dir + os.sep + dirx, help="Post files directory")

def set_about_dir(dirx):
    define("about_dir", default=options.source_dir + os.sep + dirx, help="About files directory")

def set_templates_dir(dirx):
    define("templates_dir", default=options.source_dir + os.sep + dirx, help="Templates directory, maybe not only one")

def set_current_template_dir(name):
    define("current_template_dir", default=options.templates_dir + os.sep + name, help="Current template path")

def set_static_resource_dir(dirx):
    define("static_resource_dir", default=options.current_template_dir + os.sep + dirx, help="Static resource directory")

def set_global_resource_dir(dirx):
    define("global_resource_dir", default=options.source_dir + os.sep + dirx, help="Global resource directory")

def set_root_path(root_path):
    define("root_path", default=root_path, help="Project root path")

def get_config_file(file_path):
    config = ConfigParser.RawConfigParser()
    config.read(file_path)
    return config

def load_config(file_path):
    config = get_config_file(file_path)

    set_author(config.get("sect_basic", "author"))
    set_url(config.get("sect_basic", "url"))
    set_title(config.get("sect_basic", "title"))
    set_keywords(config.get("sect_basic",  "keywords"))
    set_description(config.get("sect_basic", "description"))
    set_github_fork_link(config.get("sect_basic", "github_fork_link"))
    set_disqus_shortname(config.get("sect_basic", "disqus_shortname"))
    set_google_analytics_id(config.get("sect_basic", "google_analytics_id"))
    set_port(config.get("sect_server", "port"))
    set_source_dir(config.get("sect_dir_tree", "source_dir"))
    set_build_dir(config.get("sect_dir_tree", "build_dir"))
    set_post_dir(config.get("sect_dir_tree", "posts_dir"))
    set_about_dir(config.get("sect_dir_tree", "about_dir"))
    set_templates_dir(config.get("sect_dir_tree", "templates_dir"))
    set_current_template_dir(config.get("sect_basic", "template_name"))
    set_static_resource_dir(config.get("sect_dir_tree", "static_resource_dir"))
    set_global_resource_dir(config.get("sect_dir_tree", "global_resource_dir"))

def init_root_path(root_path):
    set_root_path(root_path)

    # change current working directory to root_path for relative paths to work correctly
    os.chdir(root_path)
    if os.access(root_path, os.F_OK):
        sys.path.append(root_path)
