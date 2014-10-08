#!/usr/bin/env python

'''
Created on Oct 6, 2014

@author: sunnycomes
'''

import os,time
from tornado.options import options
from src.common.utils import init_root_path, load_config

def formatPostTitle(tt):
    tt = tt.lower()
    
    words = tt.split(" ")
    for word in words[:]: # Do not use 'for word in words:'
        if word == "":
            words.remove("")
    
    return  '-'.join(words)
    
def getPostInfo():
    post = {}
    post_title = raw_input("Enter the title, use English anyway: ")
    post["title"] =  "\"" + post_title + "\""
    
    title = formatPostTitle(post_title)
    
    timex = time.time()
    current_timex = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timex))
    post["date"] = current_timex
    
    current_date = time.strftime('%Y-%m-%d',time.localtime(timex))
    post["post_name"] = current_date + "-" + title
    
    return post

def writeToFile(path, post):
    filex = open(path, "wb")
    content = "---\n" + "title: " + post["title"] + "\n" + "date: " + post["date"] + "\n---\n"
    filex.write(content)
    
if __name__ == '__main__':
    root_path = os.path.dirname(os.path.abspath(__file__))
    init_root_path(root_path)
    
    config_file_path = root_path + os.sep + "setup.cfg"
    load_config(config_file_path)
    
    post = getPostInfo()
    dest_dir = options.posts_dir
    
    path = dest_dir + os.sep + post["post_name"] + ".markdown"
    writeToFile(path, post)
    