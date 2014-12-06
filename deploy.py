#!/usr/bin/env python

'''
Created on Oct 7, 2014

@author: sunnycomes
'''

import os
from tornado.options import define, options

from generate import generate
from src.common.utils import init_root_path, load_config, get_config_file


def is_build_dir_exists():
    return os.path.exists(options.build_dir)

def get_in():
    os.chdir(options.build_dir)
	
def go_back():
    os.chdir(options.root_path)
	
def init():
    if is_build_dir_exists():
        os.system("git init")

def reset():
    if(is_build_dir_exists()):
        os.system("git reset --hard")
		
def add():
    os.system("git add -A")
    
def commit():
    os.system("git commit -a -m 'New changes has made.'")

def pull():
    os.system("git pull " + options.github_pages_repo + " master")
    
def push():
    os.system("git push " + options.github_pages_repo + " master")

def sync():
    if is_build_dir_exists():
        get_in()
        init()
        reset()
        pull()
        go_back()
		
def deploy():
    get_in()
    add()
    commit()
    pull()
    push()
    go_back()
    
if __name__ == '__main__':
    root_path = os.path.dirname(os.path.abspath(__file__))
    init_root_path(root_path)
    
    config_file_path = root_path + os.sep + "setup.cfg"
    load_config(config_file_path)
    
    config = get_config_file(config_file_path)
    define("github_pages_repo", default = config.get("sect_basic", "github_pages_repo"), help="github pages repo url")

    sync()
    
    generate()
    
    deploy()
    
    
    
    
