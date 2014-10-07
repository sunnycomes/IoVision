#!/usr/bin/env python

'''
Created on Oct 7, 2014

@author: sunnycomes
'''

import os
import subprocess

from tornado.options import define, options
from src.common.utils import initRootPath, loadConfig, getConfigFile
from generate import generate


def isRepoInited():
    return os.path.exists(options.build_dir)

def add():
    os.chdir(options.build_dir)
    if isRepoInited():
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
    initRootPath(root_path)
    
    config_file_path = root_path + os.sep + "setup.cfg"
    loadConfig(config_file_path)
    
    config = getConfigFile(config_file_path)
    define("github_pages_repo", default = config.get("sect_basic", "github_pages_repo"), help="github pages repo url")

    generate()
    
    deploy()
    
    
    
    