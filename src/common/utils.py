'''
Created on Oct 6, 2014

@author: sunnycomes
'''
import os, sys
import ConfigParser
from tornado.options import define, options

def set_author(author):
    define("author", default=author, help="Author of the project")

def set_url(url):
    define("url", default=url, help="Author's home page url")

def set_title(title):
    define("title", default=title, help="Site's title")
 
def set_github_link(link):
    define("github_link", default=link, help="Github source code link")

def set_disqus_shortname(name):
    define("disqus_shortname", default=name, help="Disqus shortname used to identify the site.")

def set_port(port):
    define("port", default=port, help="the port tornado listen to")
    
def set_source_dir(dirx):
    define("source_dir", default=os.getcwd() + os.sep + dirx, help="Source files directory")
    
def setBuildDir(dirx):
    define("build_dir", default=os.getcwd() + os.sep + dirx, help="Built files directory")
    
def setPostDir(dirx):
    define("posts_dir", default=options.source_dir + os.sep + dirx, help="Post files directory")

def setAboutDir(dirx):
    define("about_dir", default=options.source_dir + os.sep + dirx, help="About files directory")
       
def setTemplatesDir(dirx):
    define("templates_dir", default=options.source_dir + os.sep + dirx, help="Templates directory, maybe not only one")

def setCurrentTemplateDir(name):
    define("current_template_dir", default=options.templates_dir + os.sep + name, help="Current template path")

def setStaticResourceDir(dirx):    
    define("static_resource_dir", default=options.current_template_dir + os.sep + dirx, help="Static resource directory")
    
def getConfigFile(file_path):     
    config = ConfigParser.RawConfigParser()
    config.read(file_path)
    return config

def loadConfig(file_path):
    config = getConfigFile(file_path)
    
    set_author(config.get("sect_basic", "author"))
    set_url(config.get("sect_basic", "url"))
    set_title(config.get("sect_basic", "title"))
    set_github_link(config.get("sect_basic", "github_link"))
    set_disqus_shortname(config.get("sect_basic", "disqus_shortname"))
    set_port(config.get("sect_server", "port"))
    set_source_dir(config.get("sect_dir_tree", "source_dir"))
    setBuildDir(config.get("sect_dir_tree", "build_dir"))
    setPostDir(config.get("sect_dir_tree", "posts_dir"))
    setAboutDir(config.get("sect_dir_tree", "about_dir"))
    setTemplatesDir(config.get("sect_dir_tree", "templates_dir"))
    setCurrentTemplateDir(config.get("sect_basic", "template_name"))
    setStaticResourceDir(config.get("sect_dir_tree", "static_resource_dir"))    
       
def initRootPath(root_path):
    # change current working directory to root_path for relative paths to work correctly
    os.chdir(root_path)
    if os.access(root_path, os.F_OK):
        sys.path.append(root_path)
