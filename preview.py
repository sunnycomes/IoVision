#!/usr/bin/env PYTHON

import os, sys

from tornado.web import Application
from tornado.ioloop import IOLoop
from src.handlers import handlers
from tornado.options import options
from config_mgr import loadConfig

def initSourcePath():
    source_path = os.path.dirname(os.path.abspath(__file__))
    # change current working directory to source_path for relative paths to work correctly
    os.chdir(source_path)
    if os.access(source_path, os.F_OK):
        sys.path.append(source_path)
    
def initServer():
    settings = dict(
                    debug = True,
                    static_path=options.static_resource_dir,
                    template_path=options.current_template_dir
    )
    server = Application(handlers, **settings)
    #server.settings = settings # Never use this.    
    server.listen(options.port)

if __name__ == "__main__":
    initSourcePath()
    loadConfig()
    initServer()
    IOLoop.current().instance().start()

