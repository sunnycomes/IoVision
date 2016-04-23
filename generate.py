#!/usr/bin/env python

'''
Created on Oct 6, 2014

@author: sunnycomes
'''

import os,time
import shutil
from tornado.options import options

from src.common import post_parser
from src.common.post_parser import BasicParser, get_all_markdown_files
from src.common.settings import get_site_info, get_3rd_party_snippets
from src.common.template_parser import TemplateParser
from src.common.utils import init_root_path, load_config, mkdir, copy_in_directory

def list_template_files():
    return os.listdir(options.current_template_dir)

def generate_index():
    posts = post_parser.get_all_parsed_posts()
    params = get_site_info()
    snippets = get_3rd_party_snippets()
    html = TemplateParser.parse(options.current_template_dir, "index.html", posts=posts, params=params, snippets=snippets)

    index_file = open(options.build_dir + os.sep + "/index.html", "wb")
    index_file.write(html)

def copy_static_files():
    dest = options.build_dir + os.sep + "static"
    copy_in_directory(options.static_resource_dir, dest)

def generate_posts():
    dest = options.build_dir + os.sep + "post"
    mkdir(dest)
    posts = post_parser.get_all_parsed_posts(brief=False)
    params = get_site_info()
    snippets = get_3rd_party_snippets()
    for post in posts:
        html = TemplateParser.parse(options.current_template_dir, "post.html", post=post, params=params, snippets = snippets)
        post_file = open(dest + os.sep + post["post_name"] + ".html", "wb")
        post_file.write(html)

def copy_pdf_posts():
    for file_name in os.listdir(options.posts_dir):
        if file_name and file_name.endswith(".pdf"):
            full_path = options.posts_dir + os.sep + file_name
            shutil.copy(full_path, options.build_dir + "/post/")

def copy_pdf_about():
    for file_name in os.listdir(options.about_dir):
        if file_name and file_name.endswith(".pdf"):
            full_path = options.about_dir + os.sep + file_name
            shutil.copy(full_path, options.build_dir + "/about/")

def generate_about():
    dest = options.build_dir + os.sep + "about"
    mkdir(dest)
    post = BasicParser.parse(options.about_dir, "index.markdown")
    params = get_site_info()
    snippets = get_3rd_party_snippets()
    html = TemplateParser.parse(options.current_template_dir, "about.html", post=post, params=params, snippets=snippets)
    about_file = open(dest + os.sep + "index.html", "wb")
    about_file.write(html)

def generate_sitemap():
    post_name_list = os.listdir(options.posts_dir)
    post_name_list.sort(reverse=True)

    urlset = []
    for post_name in post_name_list:
        url_entry = {}
        new_post_name = post_name.replace("markdown", "html")
        full_path = options.posts_dir + os.sep + post_name

        url_entry['post_url'] = options.url + "/post/" + new_post_name
        url_entry['lastmod'] = time.strftime('%Y-%m-%dT%H:%M:%S+08:00', time.localtime(int(os.path.getmtime(full_path))))
        url_entry['changefreq'] = 'monthly'
        url_entry['priority'] = '1'

        urlset.append(url_entry)

    item_list = os.listdir(options.about_dir)
    item_list.sort(reverse=True)
    for item_name in item_list:
        url_entry = {}
        new_item_name = item_name.replace('markdown', 'html')
        full_path = options.about_dir + os.sep + item_name

        url_entry['post_url'] = options.url + "/about/" + new_item_name
        url_entry['lastmod'] = time.strftime('%Y-%m-%dT%H:%M:%S+08:00', time.localtime(int(os.path.getmtime(full_path))))
        url_entry['changefreq'] = 'weekly'
        url_entry['priority'] = '1'

        urlset.append(url_entry)

    index_url_entry = {}
    index_url_entry['post_url'] = options.url + "/index.html"
    index_url_entry['lastmod'] = time.strftime('%Y-%m-%dT%H:%M:%S+08:00', time.localtime(int(os.path.getmtime(options.about_dir + os.sep + "index.markdown"))))
    index_url_entry['changefreq'] = 'weekly'
    index_url_entry['priority'] = '1'

    urlset.append(index_url_entry)

    sitemap = TemplateParser.parse(options.current_template_dir, "sitemap.xml", urlset=urlset)
    sitemap_target = open(options.build_dir + os.sep + "sitemap.xml", "wb")
    sitemap_target.write(sitemap)

def copy_files_under_web_root():
    directory = options.content_dir + os.sep + "under-web-root"
    copy_in_directory(directory, options.build_dir)

def generate():
    mkdir(options.build_dir)
    generate_index()
    copy_static_files()
    generate_posts()
    copy_pdf_posts()
    generate_about()
    copy_pdf_about()
    generate_sitemap()
    copy_files_under_web_root()

if __name__ == '__main__':
    root_path = os.path.dirname(os.path.abspath(__file__))
    init_root_path(root_path)

    config_file_path = root_path + os.sep + "setup.cfg"
    load_config(config_file_path)

    generate()
