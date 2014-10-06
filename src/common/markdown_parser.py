'''
Created on Oct 4, 2014

@author: sunnycomes
'''
import os
import codecs
import markdown
from tornado.options import options

class BasicParser:
    '''
    This BasicParser is a util class dedicated to parse markdown format files
    '''
    
    @staticmethod
    def _readPost(post_path):
        post_file = codecs.open(post_path, mode='r', encoding='utf8')
        lines = post_file.readlines()
        post_file.close()     
        return lines   
    
    @staticmethod
    def _findTitle(lines):
        for line in lines:
            if line.find("title: ") == 0:
                return line[7:-1]
            
        return ""
    
    @staticmethod
    def _findDate(lines):
        for line in lines:
            if line.find("date: ") == 0 :
                return line[6:-1]
        
        return ""
    
    @staticmethod
    def _findContent(lines):
        content = ""
        startAt = 1
        for line in lines[1:]:
            startAt += 1
            if line.find("---") == 0:
                break;
        
        for line in lines[startAt:]:
            content += line
        
        return content
        
    @staticmethod
    def parse(post_dir, post_name):
        post_path = post_dir + os.sep + post_name
        lines = BasicParser._readPost(post_path)
        
        sections = {}
        sections["post_name"] = post_name[0:-9]
        sections["title"] = BasicParser._findTitle(lines)
        sections["date"] = BasicParser._findDate(lines)
        
        content = BasicParser._findContent(lines)
        sections["content"] = markdown.markdown(content)

        return sections
    
    @staticmethod
    def getBriefContent(content):
        end = content.index("<!-- more -->")
        return content[0:end]

def getAllParsedPosts():
        posts = []
        post_name_list = os.listdir(options.posts_dir)
        post_name_list.sort(reverse=True)
        
        for post_name in post_name_list:
            post = BasicParser.parse(options.posts_dir, post_name)
            post["content"] = BasicParser.getBriefContent(post["content"])
            posts.append(post)
            
        return posts