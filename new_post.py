#!/usr/bin/env python

'''
Created on Oct 6, 2014

@author: sunnycomes
'''

import os, time
from tornado.options import options

from src.common.utils import init_root_path, load_config


def format_post_title(tt):
    tt = tt.lower()
    
    words = tt.split(" ")
    for word in words[:]: # Do not use 'for word in words:'
        if word == "":
            words.remove("")
    
    return  '-'.join(words)
    
def get_post_info():
    post = {}
    post_title = raw_input("Enter the title, use English anyway: ")
    post["title"] =  "\"" + post_title + "\""
    
    title = format_post_title(post_title)
    
    timex = time.time()
    current_timex = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timex))
    post["date"] = current_timex
    
    current_date = time.strftime('%Y-%m-%d',time.localtime(timex))
    post["post_name"] = current_date + "-" + title
    
    return post

def write_to_file(path, post):
    filex = open(path, "wb")
    content = "---\n" + "title: " + post["title"] + "\n" + "date: " + post["date"] + "\n---\n"
    filex.write(content)
    
if __name__ == '__main__':
    root_path = os.path.dirname(os.path.abspath(__file__))
    init_root_path(root_path)
    
    config_file_path = root_path + os.sep + "setup.cfg"
    load_config(config_file_path)
    
    post = get_post_info()
    dest_dir = options.posts_dir
    
    path = dest_dir + os.sep + post["post_name"] + ".markdown"
    write_to_file(path, post)
    