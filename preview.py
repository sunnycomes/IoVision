#!/usr/bin/env PYTHON

from tornado.web import Application
from tornado.ioloop import IOLoop
from src.handlers import handlers
from tornado.options import options

from utils import initSourcePath, loadConfig
    
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

