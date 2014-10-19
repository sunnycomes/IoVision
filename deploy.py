#!/usr/bin/env python

'''
Created on Oct 7, 2014

@author: sunnycomes
'''

import os
from tornado.options import define, options

from generate import generate
from src.common.utils import init_root_path, load_config, get_config_file


def is_repo_inited():
    return os.path.exists(options.build_dir)

def add():
    os.chdir(options.build_dir)
    if is_repo_inited():
        os.system("git init")
    
    os.system("git add .")
    
def commit():
    os.chdir(options.build_dir)
    os.system("git commit -a -m 'New changes has made.'")

def pull():
    os.chdir(options.build_dir)
    os.system("git pull " + options.github_pages_repo + " master")
    
def push():
    os.chdir(options.build_dir)
    os.system("git push " + options.github_pages_repo + " master")

def deploy():
    
    add()
    commit()
    pull()
    push()
    
if __name__ == '__main__':
    root_path = os.path.dirname(os.path.abspath(__file__))
    init_root_path(root_path)
    
    config_file_path = root_path + os.sep + "setup.cfg"
    load_config(config_file_path)
    
    config = get_config_file(config_file_path)
    define("github_pages_repo", default = config.get("sect_basic", "github_pages_repo"), help="github pages repo url")

    generate()
    
    deploy()
    
    
    
    