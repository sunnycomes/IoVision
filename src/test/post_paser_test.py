#!/usr/bin/env python

import os

from src.common.post_parser import BasicParser

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    md = BasicParser.parse(path + os.sep + "resources", "2014-03-1-talk-about-bitcoin-change.markdown")
    print BasicParser.get_brief_content(md["content"]);
