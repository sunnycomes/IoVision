'''
Created on Oct 6, 2014

@author: sunnycomes
'''
import os, sys
import ConfigParser
from tornado.options import define, options

def setAuthor(author):
    define("author", default=author, help="Author of the project")

def setUrl(url):
    define("url", default=url, help="Author's home page url")

def setTitle(title):
    define("title", default=title, help="Site's title")
 
def setGithubLink(link):
    define("github_link", default=link, help="Github source code link")

def setDisqusShortame(name):
    define("disqus_shortname", default=name, help="Disqus shortname used to identify the site.")

def setPort(port):
    define("port", default=port, help="the port tornado listen to")
    
def setSourceDir(dirx):
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
    
def getConfigFile():     
    config = ConfigParser.RawConfigParser()
    config.read("setup.cfg")
    return config

def loadConfig():
    config = getConfigFile()
    setAuthor(config.get("sect_basic", "author"))
    setUrl(config.get("sect_basic", "url"))
    setTitle(config.get("sect_basic", "title"))
    setGithubLink(config.get("sect_basic", "github_link"))
    setDisqusShortame(config.get("sect_basic", "disqus_shortname"))
    setPort(config.get("sect_server", "port"))
    setSourceDir(config.get("sect_dir_tree", "source_dir"))
    setBuildDir(config.get("sect_dir_tree", "build_dir"))
    setPostDir(config.get("sect_dir_tree", "posts_dir"))
    setAboutDir(config.get("sect_dir_tree", "about_dir"))
    setTemplatesDir(config.get("sect_dir_tree", "templates_dir"))
    setCurrentTemplateDir(config.get("sect_basic", "template_name"))
    setStaticResourceDir(config.get("sect_dir_tree", "static_resource_dir"))    
       
def initRootPath():
    source_path = os.path.dirname(os.path.abspath(__file__))
    # change current working directory to source_path for relative paths to work correctly
    os.chdir(source_path)
    if os.access(source_path, os.F_OK):
        sys.path.append(source_path)
