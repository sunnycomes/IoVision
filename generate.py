'''
Created on Oct 6, 2014

@author: sunnycomes
'''

import os
import shutil
from tornado.options import options
from utils import initSourcePath, loadConfig
from src.common.template_parser import TemplateParser
from src.common.settings import getSiteInfo
from src.common import markdown_parser
from src.common.markdown_parser import BasicParser

def listTemplateFiles():
    return os.listdir(options.current_template_dir)

def mkdir(dirx):
    if os.path.exists(dirx):
        return
    
    os.mkdir(dirx)
    
def rmdir(dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    pass
    
def generateIndex():
    posts = markdown_parser.getAllParsedPosts()
    params = getSiteInfo()
    html = TemplateParser.parse(options.current_template_dir, "index.html", posts=posts, params=params)
    
    index_file = open("build/index.html", "wb")
    index_file.write(html)

def copyStaticFiles():
    dest = options.build_dir + os.sep + "static"
    rmdir(dest)
    shutil.copytree(options.static_resource_dir, dest)

def generatePosts():
    dest = options.build_dir + os.sep + "post"
    mkdir(dest)
    posts = markdown_parser.getAllParsedPosts(brief=True)
    params = getSiteInfo()
    
    for post in posts:
        html = TemplateParser.parse(options.current_template_dir, "post.html", post=post, params=params)
        post_file = open(dest + os.sep + post["post_name"] + ".html", "wb")
        post_file.write(html)
    
def generateAbout():  
    dest = options.build_dir + os.sep + "about"
    mkdir(dest)
    post = BasicParser.parse(options.about_dir, "about.markdown")
    params = getSiteInfo()
    
    html = TemplateParser.parse(options.current_template_dir, "about.html", post=post, params=params)
    about_file = open(dest + os.sep + "index.html", "wb")
    about_file.write(html)
    
if __name__ == '__main__':
    initSourcePath()
    loadConfig()
    
    generateIndex()
    copyStaticFiles()
    generatePosts()
    generateAbout()
    