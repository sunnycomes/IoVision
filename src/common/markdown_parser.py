'''
Created on Oct 4, 2014

@author: sunnycomes
'''
import codecs
import markdown
import os
from tornado.options import options

class BasicParser:
    '''
    This BasicParser is a util class dedicated to parse markdown format files
    '''

    @staticmethod
    def _read_post(post_path):
        post_file = codecs.open(post_path, mode='r', encoding='utf8')
        lines = post_file.readlines()
        post_file.close()
        return lines

    @staticmethod
    def _find_title(lines):
        for line in lines:
            if line.find("title: ") > -1:
                line = line.strip()
                return line[7:len(line)]

        return "No title"

    @staticmethod
    def _find_keywords(lines):
        for line in lines:
            if line.find("keywords: ") > -1:
                line = line.strip()
                return line[10:len(line)]

        return "No keywords"

    @staticmethod
    def _find_description(lines):
        for line in lines:
            if line.find("description: ") > -1:
                line = line.strip()
                return line[13:len(line)]

        return "No description"

    @staticmethod
    def _find_categories(lines):
        for line in lines:
            if line.find("categories: ") > -1:
                line = line.strip()
                return line[12:len(line)]

        return "No categories"

    @staticmethod
    def _find_date(lines):
        for line in lines:
            if line.find("date: ") > -1:
                line = line.strip()
                return line[6:len(line)]

        return "No date"

    @staticmethod
    def _find_comment_allowed(lines):
        for line in lines:
            if line.find("comment_allowed: ") > -1:
                line = line.strip()
                print(line)
                return line[17:len(line)]

        return "true"

    @staticmethod
    def _find_content(lines):
        content = ""
        startAt = 1
        for line in lines[1:]:
            startAt += 1
            if line.find("---") > -1:
                break;

        for line in lines[startAt:]:
            content += line

        return content

    @staticmethod
    def parse(post_dir, post_name):
        post_path = post_dir + os.sep + post_name
        lines = BasicParser._read_post(post_path)

        sections = {}
        sections["post_name"] = post_name[0:-9]
        sections["title"] = BasicParser._find_title(lines)
        sections["keywords"] = BasicParser._find_keywords(lines)
        sections["description"] = BasicParser._find_description(lines)
        sections["categories"] = BasicParser._find_categories(lines)
        sections["date"] = BasicParser._find_date(lines)
        sections["comment_allowed"] = BasicParser._find_comment_allowed(lines)

        content = BasicParser._find_content(lines)
        sections["content"] = markdown.markdown(content)

        return sections

    @staticmethod
    def get_brief_content(content):
        if content == "":
            return ""

        end = -1
        if content.find("<!-- more -->") != -1:
            end = content.index("<!-- more -->")

        return content[0:end]

def get_all_markdown_files(items):
    post_name_list = []

    for item in items:
        if os.path.splitext(item)[1] == ".markdown":
            post_name_list.append(item)

    return post_name_list

def get_all_parsed_posts(brief=True):
        posts = []
        items = os.listdir(options.posts_dir)
        post_name_list = get_all_markdown_files(items)
        post_name_list.sort(reverse=True)

        for post_name in post_name_list:
            post = BasicParser.parse(options.posts_dir, post_name)
            if brief:
                post["content"] = BasicParser.get_brief_content(post["content"])
            posts.append(post)

        return posts
