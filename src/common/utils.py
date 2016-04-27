'''
Created on Oct 6, 2014

@author: sunnycomes
'''
import ConfigParser
import os, sys
from tornado.options import define, options

def mkdir(dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

def rmdir(dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    pass

def copy_in_directory(src, dst):
    if not os.path.exists(dst):
        mkdir(dst)

    os.system("rsync -av --exclude='.*' " + src + " " +  dst)

def get_config_file(file_path):
    config = ConfigParser.RawConfigParser()
    config.read(file_path)
    return config

def set_root_path(root_path):
    define("root_path", default=root_path, help="Project root path")

def set_source_dir(dirx):
    define("source_dir", default=os.getcwd() + os.sep + dirx, help="Source files directory")

def set_build_dir(dirx):
    define("build_dir", default=os.getcwd() + os.sep + dirx, help="Built files directory")

def set_templates_dir(dirx):
    define("templates_dir", default=options.source_dir + os.sep + dirx, help="Templates directory, maybe not only one")

def set_current_template_dir(name):
    define("current_template_dir", default=options.templates_dir + os.sep + name, help="Current template path")

def set_static_resource_dir(dirx):
    define("static_resource_dir", default=options.current_template_dir + os.sep + dirx, help="Static resource directory")

def set_global_resource_dir(dirx):
    define("global_resource_dir", default=options.source_dir + os.sep + dirx, help="Global resource directory")

def set_content_dir(dirx):
    define("content_dir", default=os.getcwd() + os.sep + dirx, help="Content files directory")

def set_posts_dir(dirx):
    define("posts_dir", default=options.content_dir + os.sep + dirx, help="Post files directory")

def set_about_dir(dirx):
    define("about_dir", default=options.content_dir + os.sep + dirx, help="About files directory")

def load_config(file_path):
    config = get_config_file(file_path)

    for sect in ('sect_basic','sect_3rd_party_account','sect_server'):
        keys = config.get(sect, "keys")
        for key in keys.split(','):
            define(key, default=config.get(sect, key), help=key)

    set_source_dir(config.get("sect_dir_src", "source_dir"))
    set_build_dir(config.get("sect_dir_src", "build_dir"))
    set_templates_dir(config.get("sect_dir_src", "templates_dir"))
    set_current_template_dir(config.get("sect_basic", "template_name"))
    set_static_resource_dir(config.get("sect_dir_src", "static_resource_dir"))
    set_global_resource_dir(config.get("sect_dir_src", "global_resource_dir"))

    set_content_dir(config.get("sect_dir_content", "content_dir"))
    set_posts_dir(config.get("sect_dir_content", "posts_dir"))
    set_about_dir(config.get("sect_dir_content", "about_dir"))

def init_root_path(root_path):
    set_root_path(root_path)

    # change current working directory to root_path for relative paths to work correctly
    os.chdir(root_path)
    if os.access(root_path, os.F_OK):
        sys.path.append(root_path)
